# python-challenge

**PyBank Python Code**
**Make sure when running that file path in terminal is PyBank/Resources to run properly**

import csv

# Read the CSV file and store the data in lists
with open('budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    dates = []
    profits_losses = []
    for row in csv_reader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Calculate the total number of months
total_months = len(dates)

# Calculate the net total amount of "Profit/Losses"
net_total = sum(profits_losses)

# Calculate the changes in "Profit/Losses" over time
changes = [profits_losses[i] - profits_losses[i-1] for i in range(1, len(profits_losses))]

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]  # Add 1 to account for the skipped first element
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]  # Add 1 to account for the skipped first element

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the analysis results to a text file
with open('financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")



**PyPoll Python Code**
**Make sure when running that file path in terminal is PyPoll/Resources to run properly**
