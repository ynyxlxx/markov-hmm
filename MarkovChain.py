import numpy as np
import argparse

parser = argparse.ArgumentParser(description='MarkovChain')
parser.add_argument('inputdata')
parser.add_argument('filename_1')
parser.add_argument('filename_2')
args = parser.parse_args()

################################################################################
def P_MarkovChain( input_data, inside_table, outside_table):

    Ratio_table = np.log2(inside_table) - np.log2(outside_table)
    inside_table = np.log2(inside_table)
    outside_table = np.log2(outside_table)


    for i in range(len(input_data)):

        string = input_data[i]
        string = string[0]
        letters = list(string)
        P_MarkovChain_inside = 0
        P_MarkovChain_outside = 0
        P_MarkovChain_Ratio = 0

        for j in range(len(letters)):
            if letters[j] == 'A':
                letters[j] = '0'
            elif letters[j] =='C':
                letters[j] ='1'
            elif letters[j] == 'G':
                letters[j] = '2'
            elif letters[j] == 'T':
                letters[j] = '3'

        for index in range(len(letters)):
            P_MarkovChain_inside = P_MarkovChain_inside + inside_table[int(letters[index - 1])][int(letters[index])]
            P_MarkovChain_outside = P_MarkovChain_outside + outside_table[int(letters[index - 1])][int(letters[index])]
            P_MarkovChain_Ratio = P_MarkovChain_Ratio + Ratio_table[int(letters[index - 1])][int(letters[index])]

        if P_MarkovChain_Ratio > 0:
            print('for NO.' + str(i + 1) + ' sequence:')
            print(str(P_MarkovChain_Ratio) + ' inside')
        elif P_MarkovChain_Ratio < 0:
            print('for NO.' + str(i + 1) + ' sequence:')
            print(str(P_MarkovChain_Ratio) + ' outside')

    return

inside = np.loadtxt(args.filename_1, dtype = float)
print('inside table load complete.')
print(inside)
outside = np.loadtxt(args.filename_2, dtype = float)
print('outside table load complete.')
print(outside)

inputdata = []
for line in open(args.inputdata):
    str1 = line.split()
    inputdata.append(str1)
print('input data load complete.')

print('\n')
P_MarkovChain(inputdata, inside, outside)