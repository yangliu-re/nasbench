import json
import sys
import os
from os import listdir
from os.path import join

# single hash version
folder = '00'
hashes = [f for f in listdir(folder)]
h = hashes[0]
data = []
epochs = []
for i in range(1, 4):
    file = join(folder, h, 'repeat_{}/results.json'.format(i))
    data = json.load(open(file, 'rb'))
    if len(data) < len(data['evaluation_results']):
        data = [[] for _ in range(len(data['evaluation_results']))]
    if len(epochs) < len(data['evaluation_results']):
        epochs = [data['evaluation_results'][e]['epochs'] for e in range(len(data['evaluation_results']))]
    for e in range(len(data['evaluation_results'])):
        data.append(['evaluation_results'][e]['validation_accuracy'])

data = np.array(data)
for i, e in enumerate(epochs):
    print('epoch', e)
    print('data', data[i])
    print('mean', np.mean(data[i]))
    print('stdev', np.std(data[i]))