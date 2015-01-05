__author__ = 'zhuangding'
import pmid
import re

sentence = 'AB - We have previously reported the participation of the <GENE> protein kinase CK2 </GENE> in the mechanism by which salicylic acid activates transcription of genes , such as those coding for <GENE> glutathion S - transferases </GENE> , in tobacco .'

g = re.compile('\<gene\>([^\<\>]+)\<\/gene\>', re.I)
gene = g.finditer(sentence)

for m in gene:
    print(m.group(0), m.start(), m.end())