# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 19:33:07 2021

@author: Soumya
"""

"""
test_package
"""

import pandas as pd

class test_package:
    
    def __init__(self, filepath: str):
        self._df = pd.read_csv(filepath)
        
    def printDf(self):
        print(self._df)

def main():
    
    obj = test_package(filepath="F:\\rohan\\appliedaicourse\\Github\\test_package\\test.csv")
    obj.printDf()
    
if __name__=='__main__':
    main()