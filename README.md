# Billboard Hot 100 Chart Analysis (Week of Sept 12, 2026)

A data analytics mini-project using the **real, current Billboard Hot 100 top 20** — song, artist, rank, last week's rank, peak position, and weeks on chart, pulled from that week's official chart.

## Why this project
Music charts are messy, real-world, constantly-updating data — perfect for showing off cleaning, feature engineering (like calculating "movement" from two columns), and storytelling with charts.

## What's inside
- `billboard_hot100_2026-09-12.csv` — the raw dataset (top 20 songs that week + genre tags)
- `analyze_music.py` — the analysis script (pandas + matplotlib)
- 4 generated charts (`chart1`–`chart4`)

## Key findings
- **"Choosin' Texas" by Ella Langley** was No. 1, in its 46th week on the chart — a genuinely rare feat of staying power.
- **"Man I Need" by Olivia Dean** is the top 20's longevity champ at 54 weeks on the chart, despite never reaching #1 (peaked at #2).
- **14 of the top 20 songs have never hit #1** — a reminder that "hit song" and "chart-topper" are very different things.
- Country and Pop were tied for the most represented genres in the top 20 (6 songs each), but **Pop/Soul and Alternative/Pop songs stuck around the longest** on average.
- **"BbY WOW"** by Karol G was this week's biggest mover, jumping 13 spots (#29 → #16).

## How to talk about this in an interview
"I pulled the actual current Billboard Hot 100, engineered a 'weekly movement' feature from the rank and last-week columns, and used it to find the week's biggest climbers and fallers. I also looked at genre mix and chart longevity to see which genres tend to have staying power vs. quick spikes."

## Possible extensions (talk about these even if you don't build them)
- Track the full top 100 (not just top 20) for a bigger sample
- Pull weekly snapshots over a few months to build a real time-series of chart trajectories
- Add Spotify audio-feature data (tempo, energy, danceability) if you have API access, and correlate with chart longevity

## Run it yourself
```
pip install pandas matplotlib
python analyze_music.py
```
