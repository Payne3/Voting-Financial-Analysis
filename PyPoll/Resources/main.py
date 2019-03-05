import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


total_votes = 0
kahn_votes =[]
correy_votes = []
otooley_votes = []
Li_votes = []
K_percentage = 0
O_percentage = 0
L_percentage = 0
C_percentage = 0


with open(csvpath) as csvfile:


# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        total_votes += 1


        if row[2] == "Khan":
            kahn_votes.append(row[2])
        if row[2] == "Correy":
            correy_votes.append(row[2])
        if row[2] == "O'Tooley":
            otooley_votes.append(row[2])
        if row[2] == "Li":   
            Li_votes.append(row[2])


K_percentage = ((len(kahn_votes)/total_votes))*100
O_percentage = ((len(otooley_votes)/total_votes))*100
L_percentage = ((len(Li_votes)/total_votes))*100
C_percentage = ((len(correy_votes)/total_votes))*100


print(f"Total Votes: ({total_votes})")
print(f'Khan : {(round(K_percentage,4))} %  ({len(kahn_votes)})')
print(f"O'Tooley : {(round(O_percentage,4))} %  ({len(otooley_votes)})")
print(f'Li  : {(round(L_percentage,4))} %  ({len(Li_votes)})')
print(f'Correy  : {(round(C_percentage,4))} %  ({len(correy_votes)})')

