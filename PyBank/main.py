import csv
import os

def main():
    '''main function that reads in csv and prints and writes outputs budget analysis'''
    # initiate variables
    csv_read = os.path.join('Resources', 'budget_data.csv')
    csv_write = os.path.join('analysis', 'budget_analysis.txt')
    total_months = 0 
    net_total_amount = 0
    average_change = 0
    greatest_increase = float('-inf')
    greatest_decrease = float('inf')
    greatest_increase_date = 'Mon-Year'
    greatest_decrease_date = 'Mon-Year'
    prev_revenue = None
    revenue_change_ls = []

    # read the csv
    with open(csv_read) as f:
        reader = csv.reader(f)
        # skip header
        csv_header = next(f, None)
        # loop through data
        for row in reader:
            revenue = int(row[1])
            # update total months
            total_months += 1
            # update net total
            net_total_amount += revenue
            # this will skip first since there is no prev_revenue to start
            if prev_revenue is not None: 
                # calculate change in revenue
                rev_change = revenue - prev_revenue
                # append to list
                revenue_change_ls.append(rev_change)
                # update greatest increase
                if rev_change > greatest_increase:
                    greatest_increase = rev_change
                    greatest_increase_date = row[0]
                # update greatest decrease
                if rev_change < greatest_decrease:
                    greatest_decrease = rev_change
                    greatest_decrease_date = row[0]
            # update prev_revenue
            prev_revenue = revenue
    # update average_change
    average_change += round(sum(revenue_change_ls) / len(revenue_change_ls), 2)
    
    output = (
        f'Financial Analysis\n'
        f'----------------------------\n'
        f'Total Months: {total_months}\n'
        f'Total: ${net_total_amount}\n'
        f'Average Change: ${average_change}\n'
        f'Greatest Increase in Profts: {greatest_increase_date} (${greatest_increase})\n'
        f'Greatest Decrease in Profts: {greatest_decrease_date} (${greatest_decrease})\n'
    )
    
    print(output)

    with open(csv_write, "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()