# Modules
import csv

# set path for file
csvpath = "Resources/budget_data.csv"

# Initialize variables to store financial analysis results
total_months = 0
net_total = 0
profit_losses = []
months = []

# open the csv using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  

     # Read the header now first ( skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
     # Read each row of data after the header
    for row in csvreader:
        print(row)

        # Count total months
        total_months += 1

        # Calculate net total profit/Losses
        net_total += int(row[1])
        
        # Store profit/losses and months data for further analysis
        profit_losses.append(int(row[1]))
        months.append(row[0])

# Calculate changes in profit/losses and the average change
changes = [profit_losses[i + 1] - profit_losses[i] for i in range(len(profit_losses) - 1)]
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
increase_index = changes.index(greatest_increase)
decrease_index = changes.index(greatest_decrease)

# Print financial analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {months[increase_index+1]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {months[decrease_index+1]} (${greatest_decrease})")

# Write financial analysis results to a text file
with open('financial_analysis.txt', 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {months[increase_index+1]} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {months[decrease_index+1]} (${greatest_decrease})\n")

