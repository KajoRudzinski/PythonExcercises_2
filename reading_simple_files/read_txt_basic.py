# Open a file: file
file = open('reading_simple_files\something.txt', mode='r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

# #############################
# Read & print the first 3 lines
with open('reading_simple_files\sth_bigger.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# #######################
# Read csv with Numpy
import numpy as np

# Assign the filename: file
file = 'reading_simple_files\\titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file, encoding=None)

# Print out first two records of d
print(d[:2])