import numpy as np
import argparse
import math

parser = argparse.ArgumentParser(description='HMM')
parser.add_argument('fa_file')
parser.add_argument('hmm_file')
args = parser.parse_args()

################################
def str2float(str_list):
    float_numbers = []
    for num in str_list:
        float_numbers.append(float(num))

    return float_numbers

def HMM(input_data,initial_1,initial_2):

    State1 = math.log2(initial_1)
    State2 = math.log2(initial_2)
    max_path = []
    for i in range(len(input_data)):

        string = input_data[i]
        string = string[0]
        letters = list(string)
        # print(letters)

        for j in range(len(letters)):
            if letters[j] == 'A' or letters[j] =='a':
                letters[j] = '0'
            elif letters[j] =='C' or letters[j] =='c':
                letters[j] ='1'
            elif letters[j] == 'G' or letters[j] =='g':
                letters[j] = '2'
            elif letters[j] == 'T' or letters[j] =='t':
                letters[j] = '3'

        for index in range(len(letters)):
            if index == 0:
                State1 = State1 + log2E[0][int(letters[index])]
                State2 = State2 + log2E[1][int(letters[index])]

            State1 = max((State1 + log2E[0][int(letters[index])] + log2T[0][0]), (State2 + log2E[0][int(letters[index])] + log2T[0][1]))
            State2 = max((State1 + log2E[1][int(letters[index])] + log2T[1][0]), (State2 + log2E[1][int(letters[index])] + log2T[1][1]))

            if State1 > State2:
                max_path.append('A')
            else:
                max_path.append('B')

    change_point_start = 1
    for x in range(1, len(max_path)):
        if max_path[x-1] != max_path[x]:
            change_point = x-1
            print(str(change_point_start) + ' ' + str(change_point) + ' state' + str(max_path[x-1]))
            change_point_start = change_point + 1
    return
########################## load data from .hmm file and .fa file
print('loading .hmm file.... ')
hmm_factor = []
for line in open(args.hmm_file):
    str_e = line.split()
    hmm_factor.append(str_e)

temp = hmm_factor[1]
state1_initial =float(temp[0])
state2_initial = float(temp[1])

table1 = hmm_factor[2]
table2 = hmm_factor[3]

Emission_table = [table1[2:6],
                  table2[2:6]]
Transition_table = [table1[0:2],
                    table2[0:2]]

for i in range(len(Emission_table)):
    Emission_table[i] = str2float(Emission_table[i])
for i in range(len(Transition_table)):
    Transition_table[i] = str2float(Transition_table[i])

log2E = np.log2(Emission_table)
log2T = np.log2(Transition_table)
print('.hmm loaded.\n')

print('loading .fa file.......')
inputdata = []
for line in open(args.fa_file):
    str_i = line.split()
    inputdata.append(str_i)
inputdata.pop(0)
print('.fa file loaded.\n')

print('generate HMM......\n')
HMM(inputdata,state1_initial,state2_initial)