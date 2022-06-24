#slipi file sorter made at long last
import os
import shutil
import datetime

path = 'C:\\Users\\Baker\\Documents\\Slippi'

#makes sure it's only grabbing files that we want to be sorted 
def unsorted(path):
    
    files = os.listdir(path)
    #reads through list backwards. Allows for popping items off the list to work
    for file in range(len(files) -1,-1,-1):
        #removes things that are not slippi games from the list
        if 'Game' not in files[file]:
            files.pop(file)
    return files

def file_date(path,files):
    
    date_list = []
    #file creation date
    for file in range(len(files)):
        #gets creation time from the files
        c_time = os.path.getctime(f'{path}\\{files[file]}')
        #sets creation time to a datetime variable
        dt_c = datetime.datetime.fromtimestamp(c_time)
        #adds datetimes to a seperate list
        date_list.append(dt_c)
    return date_list


def sorting(path,c_date,files):

    compare_date = datetime.datetime.today()
    #compares value of game date to today's date
    for date in range(len(c_date)):
        if c_date[date] < compare_date:
            #attempts to create a folder. If that fails it sorts the file into the correct folder 
            try:
                os.mkdir(f'{path}\\{c_date[date].year}-{c_date[date].month}')
                shutil.move(files[date], f'{path}\\{c_date[date].year}-{c_date[date].month}')
            except:
                shutil.move(files[date], f'{path}\\{c_date[date].year}-{c_date[date].month}')
            

if __name__ == '__main__':
    files = unsorted(path)
    c_date = file_date(path, files)
    sorting(path,c_date,files)