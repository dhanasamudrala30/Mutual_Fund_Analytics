import pandas as pd

performance = pd.read_csv(
    "../data/processed/clean_scheme_performance.csv"
)

risk = input(
    "Enter Risk Appetite (Low / Moderate / Moderately High / High / Very High): "
).strip()

recommendation = performance[
    performance["risk_grade"].str.lower() == risk.lower()
]

recommendation = recommendation.sort_values(
    by="sharpe_ratio",
    ascending=False
)

recommendation = recommendation[
    [
        "scheme_name",
        "fund_house",
        "category",
        "risk_grade",
        "sharpe_ratio",
        "return_3yr_pct"
    ]
].head(3)

if recommendation.empty:
    print("No funds found for the selected risk appetite.")
else:
    print("\nTop 3 Recommended Funds:\n")
    print(recommendation)