print('...Importing Libraries...')

import pandas as pd
import numpy as np

#Create Basic Word Counter
print('...Creating Word Counter...')
def countWords(words):
    word_table = {}
    for word in words:
            if word in word_table:
                word_table[word] += 1
            else:
                word_table[word] = 1
            count = words.count(word)
            word_table[word] = count
    return sorted(word_table.items(), key=lambda item: item[1], reverse=True)

#Create Word Grabber
print('...Creating Word Grabber')
def grabWords(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    return words

#Test the Word Grabber
testwords = grabWords('/data/cat-descriptions_120396.txt')

countWords(testwords)

print('...Creating output file...')
#Create an output file
def writeOutput(filename, table):
     with open(filename, 'w') as f:
         for word, count in table:
             f.write("%s %s\n" % (word, count))

output = countWords(testwords)

writeTable('output.txt', output)

print("Output Printed!")
