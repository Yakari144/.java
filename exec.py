import os

# function that goes through the contente of the file and adds a new line with the string specified
def add_line(file, string):
    # open the file in read mode
    with open(file, 'a') as f:
        f.write('\n'+string)

# get the current directory
dirname = os.path.abspath(__file__)

# string with the path to .bashrc
bashrc = os.path.expanduser('~/.bashrc')

add_line(bashrc,'python3 '+dirname+'/binding.py\n')

