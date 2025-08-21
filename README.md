
# Global Poverty Prediction and Inequality Mapping (SDG 1: No Poverty)

## Problem Statement
SDG 1 aims to end poverty in all its forms everywhere. This project analyzes global trends in extreme poverty rates using socioeconomic indicators to predict future reductions and highlight regional disparities.

## Data Source & Ethics Disclaimer
- Source: World Bank Poverty Headcount Ratio at $2.15 a day: https://data.worldbank.org/indicator/SI.POV.DDAY (Download as ZIP containing CSV)
- Ethics: Data is aggregated and public; potential biases include underrepresentation of low-income regions or informal economies. No personal data used. Limitations: Historical data may not capture recent events like crises. Ensure ethical use by addressing biases in analysis.

## Methods Used
- EDA: Pandas for cleaning, Matplotlib/Seaborn for visuals.
- Modeling: Time series forecasting (ARIMA with statsmodels), clustering (KMeans with scikit-learn), geospatial visualization (folium).
Plain-language: We clean the data, explore patterns, build models to predict or analyze outcomes, and visualize results for clarity.

## Key Findings
- [Placeholder: Add key insights after analysis, e.g., "Poverty rates declined 10% in Asia (see figure in results/)."]
- Plain-language summary: [Placeholder: Simple explanation for non-experts, e.g., "This shows how poverty is changing worldwide."]

[Include alt-text for visuals: "Line chart showing trends by region, using colorblind-friendly palette."]

## How to Reproduce
1. Clone repo: `git clone [url]`
2. Install deps: `pip install -r requirements.txt`
3. Download data: Follow links in data/data_sources.md (or run src/download_data.py if available)
4. Run notebook: `jupyter notebook notebooks/main.ipynb`
5. Optional: Run dashboard: `streamlit run src/app.py`

## Future Improvements
- Integrate real-time API data for updates.
- Add multilingual support in documentation.
- Explore extensions like incorporating user-contributed data via PRs.
- Enhance bias mitigation with advanced fairness libraries.
