import csv
import os

def main():
    '''function to analyze election data'''
    # initiate variables
    csv_read = os.path.join('Resources', 'election_data.csv')
    csv_write = os.path.join('analysis', 'election_analysis.txt')
    total_votes = 0
    winner = None
    # dictionary for candidate and count of votes
    candidate_votes = {}

    #read csv
    with open(csv_read, 'r') as f:
        reader = csv.reader(f)
        #skip header
        csv_header = next(f, None)
        
        for row in reader:
            total_votes += 1
            candidate = row[2]
            if candidate not in candidate_votes.keys():
                candidate_votes[candidate] = 1
            else:
                candidate_votes[candidate] += 1
    
    output = (
        f"Election Results\n"
        f'-------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'-------------------------\n'
    )
    max_votes = float('-inf')
    for candidate, votes in candidate_votes.items():
        votes_percent = votes / total_votes * 100
        output = output + f'{candidate}: {votes_percent:.3f}% ({votes})\n'
        
        if votes > max_votes:
            winner = candidate

        max_votes = votes
    
    output = output + (f'-------------------------\n'
                       f'Winner: {winner}\n'
                       f'-------------------------\n'
    )

    print(output)

    with open(csv_write, "w") as f:
        f.write(output)

if __name__ == '__main__':
    main()