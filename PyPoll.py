#import modules
import os
import csv

#set variables
vote_cast = 0
candidates = []
candidate_dict ={}


#read in csv file
with open("Py_Poll_data.csv") as csv_file:

    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)


    for r in csv_reader:
        #count total number of votes
        vote_cast += 1
    

        if r[2] in candidate_dict:
            candidate_dict[r[2]] += 1

        else:
            candidate_dict[r[2]]= 1
    
    

    print(f'Election Results')
    print(f'-----------------------')
    print(f'Total Votes: {vote_cast}')
    print(f'-----------------------')

    for can in candidate_dict.items():
        name = can[0]
        percentage = can[1]/vote_cast*100

        print(f'{name}: {percentage:.3f}% ({can[1]})')

    print(f'-----------------------')
    
    max_key = max(candidate_dict, key=candidate_dict.get)
    print(f'Winner: {max_key}')
    print(f'-----------------------')


output_path = os.path.join("PyPollOutput.text")
with open(output_path, 'w', newline='') as csvwriter:

    csvwriter.write(f'Election Results\n')
    csvwriter.write(f'-----------------------\n')
    csvwriter.write(f'Total Votes: {vote_cast}\n')
    csvwriter.write(f'-----------------------\n')

    for can in candidate_dict.items():
        name = can[0]
        percentage = can[1]/vote_cast*100

        csvwriter.write(f'{name}: {percentage:.3f}% ({can[1]})\n')

    csvwriter.write(f'-----------------------\n')
    
    max_key = max(candidate_dict, key=candidate_dict.get)
    csvwriter.write(f'Winner: {max_key}\n')
    csvwriter.write(f'-----------------------\n')

