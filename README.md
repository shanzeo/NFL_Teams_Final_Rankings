# NFL_Teams_Final_Rankings

## Project Overview
This project aims to predict NFL teams' win/loss ratios using historical team performance data from 2003 to 2023. By analyzing in-game statistics and various performance metrics, we develop predictive models to estimate winning percentages for NFL teams.

## Team Members
- Aidana Bekbulatkyzy
- Alishbah Farhan
- Ben Forbes
- Nick McComb
- Shanze Owais

**Course:** CSE 482  
**Date:** February 18, 2026

## Dataset
The project utilizes a publicly available dataset from Kaggle containing NFL team statistics from the 2003 through 2023 seasons. The data includes comprehensive team performance metrics across 20 seasons.

### Data Source
- **File:** `team_stats_2003_2023.csv`
- **Rows:** 672
- **Columns:** 35
- **Teams:** All 32 NFL teams represented across multiple seasons

### Features Included
- Team identifiers and season information
- Outcome variables (wins, losses)
- Offensive statistics
- Defensive statistics
- Penalty metrics
- Efficiency metrics

## Technical Implementation

### Data Storage
The dataset has been imported into a SQLite database (`nfl_stats.db`) for efficient long-term storage and querying capabilities.

### Data Preprocessing
Initial data cleaning revealed:
- Complete numerical data in most columns
- All 672 rows contain missing values in the "ties" column (expected, as regular season ties are rare)
- No other significant missing data issues identified

## Methodology

### Model Development
1. **Data Splitting**: Partition data into training and testing sets
2. **Regression Models**: Implement various regression algorithms to predict winning percentages
3. **Model Evaluation**: Assess performance using:
   - Root Mean Square Error (RMSE)
   - Mean Absolute Error (MAE)
   - R-squared values

### Analysis Components
- Feature importance analysis to identify key predictors of team success
- Correlation matrices to understand relationships between variables
- Visualization of prediction results vs. actual outcomes
