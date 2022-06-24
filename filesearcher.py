#File searcher being created for doc control
import os
import shutil
import datetime

path = input('C:\\Users\\zkaufman\\Documents')

#makes sure it's only grabbing files that we want to be sorted 
def unsorted(path):
    
    files = os.listdir(path)
    return files

#def searching(path, files):



            

if __name__ == '__main__':
    files = unsorted(path)
    print(files)