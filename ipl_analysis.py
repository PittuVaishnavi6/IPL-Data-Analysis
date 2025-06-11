# IPL DATA ANALYSIS PROJECT
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV files
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

# Show first 5 rows of each file
print("Top 5 rows of MATCHES data:")
print(matches.head())

print("\nTop 5 rows of DELIVERIES data:")
print(deliveries.head())

# Show data dimensions
print(f"\nMatches data shape: {matches.shape}")
print(f"Deliveries data shape: {deliveries.shape}")

# Number of seasons
print("\nTotal Seasons Played:", matches['season'].nunique())

# Total number of matches
print("Total Matches Played:", matches['id'].nunique())

# Top 5 winning teams
print("\nTop 5 Winning Teams:")
print(matches['winner'].value_counts().head(5))

# Plot: Matches won by each team
plt.figure(figsize=(10,6))
sns.countplot(data=matches, y='winner', order=matches['winner'].value_counts().index, palette='Set2')
plt.title("Matches Won by Each Team")
plt.xlabel("Wins")
plt.ylabel("Teams")
plt.tight_layout()
plt.show()

# Toss decision vs winning
plt.figure(figsize=(8,5))
sns.countplot(data=matches, x='toss_decision', hue='winner')
plt.title("Toss Decision vs Winning Team")
plt.tight_layout()
plt.show()

# Most Player of the Match awards
top_players = matches['player_of_match'].value_counts().head(10)
print("\nTop 10 Players with Most 'Player of the Match' Awards:")
print(top_players)

plt.figure(figsize=(10,5))
sns.barplot(x=top_players.values, y=top_players.index, palette='coolwarm')
plt.title("Top 10 'Player of the Match' Winners")
plt.xlabel("Number of Awards")
plt.ylabel("Player")
plt.tight_layout()
plt.show()

# Top venues
venue_counts = matches['venue'].value_counts().head(10)
print("\nTop 10 IPL Venues:")
print(venue_counts)

plt.figure(figsize=(10,5))
sns.barplot(y=venue_counts.index, x=venue_counts.values, palette='magma')
plt.title("Top 10 Venues by Number of Matches")
plt.xlabel("Match Count")
plt.ylabel("Venue")
plt.tight_layout()
plt.show()

# Print column names to confirm structure
print("\nDELIVERIES columns are:", deliveries.columns.tolist())

# Top batsmen by balls faced (note: now using 'batter' instead of 'batsman')
top_batsmen = deliveries['batter'].value_counts().head(10)
print("\nTop 10 Batsmen by Balls Faced:")
print(top_batsmen)

# Top batsmen by total runs scored
batsman_runs = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Run Scorers in IPL:")
print(batsman_runs)

plt.figure(figsize=(10,5))
sns.barplot(x=batsman_runs.values, y=batsman_runs.index, palette='crest')
plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Total Runs")
plt.ylabel("Batsman")
plt.tight_layout()
plt.show()
