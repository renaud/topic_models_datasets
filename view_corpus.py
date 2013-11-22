#!/usr/bin/python
import sys
'''
Reads and displays a corpus in LDA-C format
arg1: corpus_file
arg2: vocab_file, one word per line

the LDA-C format:

    [M] [term_1]:[count] [term_2]:[count] ...  [term_N]:[count]

where `[M]` is the number of unique terms in the document, and the
`[count]` associated with each term is how many times that term appeared
in the document.

@author renaud@apache.org 20131121
'''

corpus_file = sys.argv[1]
vocab_file  = sys.argv[2]

vocab = []
with open(vocab_file) as f:
    for line in f.readlines():
        vocab.append(line.strip())
print 'vocab_file loaded, {} words\n'.format(len(vocab))

with open(corpus_file) as f:
    for id, line in enumerate(f.readlines()):
        print "doc#{} ".format(id),
        # skip first
        for token in line.strip().split(' ')[1:]:
            word = vocab[int(token.split(':')[0])]
            cnt = token.split(':')[1]
            print '{}({}) '.format(word, cnt),
        print "\n"
