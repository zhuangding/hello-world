__author__ = 'zhuangding'

import re

def gene():
    print('!!!')

class PMID():

    def __init__(self, pmid, sentence):
        self.pmid = pmid
        self.sentence = sentence

    def gene(self):
        for line in self.sentence:
            self.gene = re.findall('\<gene\>')




