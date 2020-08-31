"""
Exercise 3: Write a program to read through a mail log, build
a histogram using a dictionary to count how many messages have
come from each email address, and print the dictionary.
"""
fname = input('Enter file name: ')
if len(fname) < 1 :
    fhandle = open('mbox-short.txt')
else:
    try:
        fhandle = open(fname)
    except:
        print('Invalid file')
        quit()

daycount = dict()

for lines in fhandle :
    lines = lines.rstrip()
    words = lines.split()
    if len(words) < 3 : continue
    if words[0] != 'From' : continue
    day = words[1]
    #print(day)
    if day not in daycount :
        daycount[day] = 1
    else:
        daycount[day] += 1
print(daycount)
