"""
Billboard Hot 100 Chart Analysis — Week of September 12, 2026
----------------------------------------------------------------
Data source: Billboard Hot 100 top 20, week dated 9/12/2026.
A fun, portfolio-worthy data analytics project for music lovers.

What this script does:
1. Loads the current Hot 100 top 20
2. Analyzes genre mix, chart longevity, and movement (climbers vs fallers)
3. Builds 4 visualizations
4. Prints quick insights
"""

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------------
df = pd.read_csv("billboard_hot100_2026-09-12.csv")
df["movement"] = df["last_week"] - df["rank"]  # positive = climbed, negative = fell
df["status"] = df["movement"].apply(lambda m: "Climbing" if m > 0 else ("Falling" if m < 0 else "Holding"))

print("="*60)
print("BILLBOARD HOT 100 — WEEK OF SEPT 12, 2026 (TOP 20)")
print("="*60)

# ------------------------------------------------------------------
# 2. QUICK INSIGHTS
# ------------------------------------------------------------------
print(f"\nNo. 1 song: '{df.iloc[0]['song']}' by {df.iloc[0]['artist']} "
      f"({df.iloc[0]['weeks_on_chart']} weeks on chart)")

longest_running = df.loc[df["weeks_on_chart"].idxmax()]
print(f"Longest-running top-20 hit: '{longest_running['song']}' by {longest_running['artist']} "
      f"— {longest_running['weeks_on_chart']} weeks on the chart")

biggest_climber = df.loc[df["movement"].idxmax()]
print(f"Biggest climber this week: '{biggest_climber['song']}' by {biggest_climber['artist']} "
      f"(up {biggest_climber['movement']} spots, from #{biggest_climber['last_week']} to #{biggest_climber['rank']})")

genre_counts = df["primary_genre"].value_counts()
print("\nGenre breakdown of the Top 20:")
print(genre_counts)

never_peaked_1 = df[df["peak_position"] > 1]
print(f"\n{len(never_peaked_1)} of the top 20 songs have NEVER hit #1 (peak position > 1),")
print("showing how hard it is to reach the very top even as a hit song.")

avg_weeks_by_genre = df.groupby("primary_genre")["weeks_on_chart"].mean().sort_values(ascending=False)
print("\nAverage weeks-on-chart by genre (which genres have more staying power?):")
print(avg_weeks_by_genre.round(1))

# ------------------------------------------------------------------
# 3. VISUALIZATIONS
# ------------------------------------------------------------------
plt.style.use("seaborn-v0_8-whitegrid")

# Chart 1: Genre breakdown pie chart
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(genre_counts.values, labels=genre_counts.index, autopct="%1.0f%%", startangle=90)
ax.set_title("Genre Mix of the Billboard Hot 100 Top 20\n(Week of Sept 12, 2026)")
plt.tight_layout()
plt.savefig("chart1_genre_mix.png", dpi=150)
plt.close()

# Chart 2: Weeks on chart vs peak position (scatter) - who's a hit-and-run vs a slow burn?
fig, ax = plt.subplots(figsize=(9, 6))
scatter = ax.scatter(df["weeks_on_chart"], df["peak_position"], s=120,
                      c=df["rank"], cmap="viridis_r")
for _, row in df.iterrows():
    ax.annotate(row["song"], (row["weeks_on_chart"], row["peak_position"]),
                fontsize=8, xytext=(5, 5), textcoords="offset points")
ax.invert_yaxis()  # rank 1 at top
ax.set_xlabel("Weeks on Chart")
ax.set_ylabel("Peak Chart Position")
ax.set_title("Slow Burns vs Instant Hits: Weeks on Chart vs Peak Position")
cbar = plt.colorbar(scatter)
cbar.set_label("Current Rank")
plt.tight_layout()
plt.savefig("chart2_longevity_vs_peak.png", dpi=150)
plt.close()

# Chart 3: This week's movers - bar chart of rank change
fig, ax = plt.subplots(figsize=(9, 6))
plot_df = df.sort_values("movement")
colors = plot_df["movement"].apply(lambda m: "#2a9d8f" if m > 0 else ("#e76f51" if m < 0 else "#adb5bd"))
ax.barh(plot_df["song"] + " — " + plot_df["artist"], plot_df["movement"], color=colors)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_xlabel("Spots Moved (negative = fell, positive = climbed)")
ax.set_title("Chart Movement This Week (Top 20)")
plt.tight_layout()
plt.savefig("chart3_weekly_movers.png", dpi=150)
plt.close()

# Chart 4: Average weeks-on-chart by genre
fig, ax = plt.subplots(figsize=(8, 5))
avg_weeks_by_genre.plot(kind="bar", ax=ax, color="#6a4c93")
ax.set_ylabel("Average Weeks on Chart")
ax.set_title("Chart Staying Power by Genre")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("chart4_genre_longevity.png", dpi=150)
plt.close()

print("\nSaved 4 charts: chart1_genre_mix.png, chart2_longevity_vs_peak.png,")
print("chart3_weekly_movers.png, chart4_genre_longevity.png")
print("="*60)
