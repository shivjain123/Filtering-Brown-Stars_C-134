import pandas as pd

df = pd.read_csv('Stars/CSV Files/Stars_with_Gravity.csv')

df.drop(["Unnamed: 0"], axis=1, inplace=True)

new_df = df.loc[df["Distance"] <= 100]
main_df = new_df.loc[df["Gravity"] > 150.0]
final_df = main_df.loc[df["Gravity"] < 350.0]

df.to_csv('Stars/CSV Files/filtered.csv')