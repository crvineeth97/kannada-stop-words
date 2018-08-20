import nltk
nltk.download('punkt')
from textblob import TextBlob as tb
import json
import math
import sys

class TfIdf:

    def __init__(self, corpusPath):
        self.cps = corpusPath
        self.corpus = ""
        self.wordDfDict = {}
        self.blobList = []
        self.blobListLength = 0


    def setup(self):
        for cp in self.cps:
            self.corpus = json.load(open(cp, 'r'))
            self.buildCorpus()
        self.calculateWordFrequency()

    def buildCorpus(self):
        for i in range(0,len(self.corpus)):
            content = '. '.join(self.corpus[i]['content'])
            content.replace('..','.')
            self.blobList.append(tb(content))
        self.blobListLength = len(self.blobList)

    def calculateWordFrequency(self):
        for i, blob in enumerate(self.blobList):
            for word in set(blob.words):
                if word not in self.wordDfDict:
                    self.wordDfDict[word] = 0
                self.wordDfDict[word] += 1

    def writeToFile(self):
        outfileName = "stop-words.txt"
        outFile = open(outfileName, 'w')
        
        for key, val in sorted(self.wordDfDict.items(), key=lambda x: x[1], reverse=True)[:102]:
            outFile.write(key)
            outFile.write('\n')
            # outFile.write(str(val))
            # outFile.write('\n')
        outFile.close()

corpusPath = ["udayavani.json"]
t = TfIdf(corpusPath)
t.setup()
t.writeToFile()
