import os

import csv

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
outputpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data_result.txt')

'Define variables'
total_votes = 0

candidates = {}

with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    'read the header'
    csv_header = next(csv_reader)

    for row in csv_reader:
        'Check candidate already exist in Dictionary'
        if row[2] not in candidates:
            candidates.update({row[2]: 1})
        else:
            'Adding count of Candidate'
            temp_add_count = candidates[row[2]] + 1
            candidates[row[2]] = temp_add_count
        'Counting total votes'
        total_votes = total_votes + 1

winner = ""
candidate_vote_total=0
#rint(candidates)

with open(outputpath, "w") as outputfile:
    print("Election Results \n")
    outputfile.write("Election Results \n")
    print("-----------------------")
    outputfile.write("-----------------------\n")
    print(f"Total Votes: {total_votes}")
    outputfile.write(f"Total Votes: {total_votes}\n")
    print("-----------------------")
    outputfile.write("-----------------------\n")

    for key, value in candidates.items():
        vote_per = (value/total_votes) * 100
        print("{0} {1:.3f}% ({2})".format(key, vote_per, value))
        outputfile.write("{0} {1:.3f}% ({2})\n".format(key, vote_per, value))
        if value > candidate_vote_total:
            candidate_vote_total = value
            winner = key

    print("--------------------------")
    outputfile.write("--------------------------\n")
    print(f"Winner: {winner}")
    outputfile.write(f"Winner: {winner}\n")
    print("--------------------------")
    outputfile.write("--------------------------\n")
    outputfile.close()