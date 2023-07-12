import csv
import os

# Set the file path for the CSV file
file_path = os.path.join(".", "election_data.csv")

# Initialize variables and data structures to store the required information
total_votes = 0
candidates = {}

# Read the CSV file and iterate through each row to analyze the data
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won
percentages = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    percentages[candidate] = percentage

# Find the winner based on popular vote
winner = max(candidates, key=candidates.get)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = os.path.join(".", "election_results.txt")
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
