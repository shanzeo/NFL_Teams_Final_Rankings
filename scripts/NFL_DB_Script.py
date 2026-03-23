# LLM-Generated script to parse CSV file and import to SQL database

import csv
import sqlite3
from pathlib import Path

CSV_FILE = "team_stats_2003_2023.csv"
DB_FILE = "team_stats.db"
TABLE_NAME = "team_stats"

def import_csv_to_sqlite(csv_file, db_file, table_name):
    csv_path = Path(csv_file)
    db_path = Path(db_file)

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        if not header:
            raise ValueError("CSV file is empty or missing header row.")

        # Clean column names (remove spaces, etc.)
        columns = [col.strip().replace(" ", "_") for col in header]

        # Create SQL table schema (all TEXT for safety)
        col_defs = ", ".join(f'"{col}" TEXT' for col in columns)
        create_table_sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({col_defs});'

        placeholders = ", ".join(["?"] * len(columns))
        insert_sql = f'INSERT INTO "{table_name}" VALUES ({placeholders});'

        with sqlite3.connect(str(db_path)) as conn:
            conn.execute(create_table_sql)

            batch = []
            BATCH_SIZE = 2000

            for row in reader:
                # Ensure row length matches header
                row = (row + [None] * len(columns))[:len(columns)]
                batch.append(row)

                if len(batch) >= BATCH_SIZE:
                    conn.executemany(insert_sql, batch)
                    batch.clear()

            if batch:
                conn.executemany(insert_sql, batch)

            conn.commit()

    print(f"Imported CSV into {db_file} successfully.")

if __name__ == "__main__":
    import_csv_to_sqlite(CSV_FILE, DB_FILE, TABLE_NAME)
