# -*- coding: utf-8 -*-

import string
import json
# if you are using python 3, you should 
import urllib.request 
#import urllib2
import codecs
import re
# change the url according to your own corename and query

inputfilePath = "D:\\SubjectDetails\\InformationRetrieval\\Proj3\\project3_data\\project3_data\\queries.txt"

with codecs.open(inputfilePath,"r","utf-8") as f:
    queryfile = f.readlines()
    
f.close()

queryIDs = []
queries = []

for item in queryfile:
    trem = item.split(" ",1)
    queryIDs.append(trem[0])
    queries.append(trem[1])


queries

queries = [urllib.parse.quote_plus(ut) for ut in queries]
r = ("headline:Obama^4 Health^2 Care^1")

r = r.replace(" : ",":")
text_parts = r.split(":")
text2 = text_parts[1].split(" ")

textq = ""
for o in range(0,len(text2)):
    if((len(text2)-o) != 0):
        text2[o] = text2[o] +"^"+str(len(text2)-o)
    else:
        text2[o] = text2[o] +"^"+str(1)
    
    textq = textq+text2[o]+" "    

textq = text_parts[0] + ":" + textq

e =   urllib.parse.quote_plus(textq) 
 
inurl = "http://3.16.150.132:8983/solr/IRF19P4/select?q="+e+"&fl=id%2Cscore&wt=json&indent=true&rows=20"
outfn = 'D:\\SubjectDetails\\InformationRetrieval\\Proj3\\project3_data\\project3_data\\Mod1Docs\\InputTREC_EvalMod1.txt'


# change query id and IRModel name accordingly
qid = queryIDs[i]
IRModel='default'
outf = open(outfn, 'a+')
#data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
data = urllib.request.urlopen(inurl).read()
data1 = str(data.decode("utf-8"))
datFin = json.loads(data1)

docs = datFin['response']['docs']

# the ranking should start from 1 and increase
rank = 1
for doc in docs:
    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
    rank += 1
outf.close()
