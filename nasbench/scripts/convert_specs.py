
import pickle
import json
import numpy as np


# convert between two different formats of nasbench representation

# example input:
#[{'epochs': 0, 'spec': {'matrix': array([[0, 1, 1, 1, 1, 0, 1],
#       [0, 0, 0, 1, 1, 0, 0],
#       [0, 0, 0, 1, 0, 0, 0],
#       [0, 0, 0, 0, 1, 0, 0],
#       [0, 0, 0, 0, 0, 0, 1],
#       [0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0]], dtype=int8), 'ops': ['input', 'conv3x3-bn-relu', 'maxpool3x3', 'conv3x3-bn-relu', \
#'conv1x1-bn-relu', 'conv3x3-bn-relu', 'output']}, 

# example output:
#{"00000000000000000000000000000000": [[[0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]], [-1, 0, 2, 0, 1, 2, -2]]}


arches_11 = pickle.load(open('out_11_adjacency_0.pkl', 'rb'))
arches_13 = pickle.load(open('out_13_adjacency_0.pkl', 'rb'))


arches = []

for i in range(10):
    arches.append(arches_11[i])
    arches.append(arches_13[i])

hash_start = "000000000000000000000000000000" # minus two
arch_dict = {}

for i, arch in enumerate(arches):
    matrix = arch['spec']['matrix']
    ops = arch['spec']['ops']
    print(matrix)
    print(ops)

    op_list = [-1]
    for j in range(1,6):
        if ops[j] == 'conv3x3-bn-relu':
            op_list.append(0)
        elif ops[j] == 'conv1x1-bn-relu':
            op_list.append(1)
        else:
            op_list.append(2)
    op_list.append(-2)

    matrix = matrix.tolist()

    if i < 10:
        h = hash_start + '0' + str(i)
    elif i < 100:
        h = hash_start + str(i)

    print('converted')
    print(matrix)
    print(op_list)

    arch_dict[h] = [matrix, op_list]

with open('out_11_13_adjacency_0.json', 'w') as outfile:
    json.dump(arch_dict, outfile)
