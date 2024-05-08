import csv

# Define variables to store election data
total_votes = 0
candidates = {}
winner = ''
max_votes = 0

# Open the election data CSV file
with open("Resources/election_data.csv") as file:
    next(file)  # Skip header row
    for line in file:
        total_votes += 1
        voter_id, county, candidate = line.strip().split(',')

        # Update candidate votes count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Find the winner of the election based on popular vote
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the election results to a text file
with open('election_results.txt', 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        txtfile.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
