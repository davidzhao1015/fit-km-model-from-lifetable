#================================================================#
# Fit Kaplan-Meier Curve from published lifetable of ILD data    #
#================================================================#


# -- - Imports --- #
from turtle import color # fit Kaplan-Meier curve for ILD data
import lifelines
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# --- Raw table ---#
pm_year = [745, 592, 382, 262, 171, 97]

data = {
    "year": [0, 1, 2, 3, 4, 5],
    "survivors": pm_year
}
df = pd.DataFrame(data)


# --- Compute events per interval --- #
df["events"] = df["survivors"].shift(1) - df["survivors"]
df.loc[0, "events"] = 0  # no event at time 0
print(df)


# --- Create expanded individual-level dataset for lifelines --- #
records = []
for _, row in df.iterrows():
    year = row["year"]
    events = int(row["events"])
    # event cases
    for i in range(events):
        records.append({"time": year, "event": 1})
    # censored: the remaining survivors at last time point
    # lifelines requires censoring only at final time
    # so we add the final 62 as censored at 5 years
for i in range(int(df.iloc[-1]["survivors"])):
    records.append({"time": 5, "event": 0})

df_long = pd.DataFrame(records)
print(df_long.head())


# --- Fit Kaplan-Meier --- #
from lifelines import KaplanMeierFitter

km = KaplanMeierFitter()
km.fit(durations=df_long["time"], event_observed=df_long["event"])

# Output survival table
print(km.survival_function_)

print("Median Survival Time:", km.median_survival_time_)


# --- Plot --- #
km.plot_survival_function()
plt.title("Kaplan-Meier Survival Curve")
plt.xlabel("Time (years)")
plt.ylabel("Survival Probability")
plt.ylim(0, 1)
plt.grid()
plt.show()