#File searcher being created for doc control
import os


path = os.getcwd()

#makes sure it's only grabbing files that we want to be sorted 
def unsorted(path):
    
    files = os.listdir(path)
    return files

def search_files(found_files):

    search = input('What is the name of the file you are searching for? ')
    for file in range(len(files)):
        if search in files[file]:
            found_files.append(files[file])
    return found_files

if __name__ == '__main__':
    found_files = []
    files = unsorted(path)
    files = search_files(found_files)
    print(files)
    cont = input("Would you like to keep searching? ")
    if cont == "yes":
        hunting = search_files(found_files)
        print(hunting)
    else:
        print("Have a nice day")
        
    