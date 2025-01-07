# •Read /var/log/messages or any other file that you prefer
# •Find all the logs which pertain to USB (or choose other keywords) and print them out selectively
# •Try to filter out fields within the log line

import csv

# Write
print("First task:")
f = open("tekstaDoku.txt","w") # Users\\andazidele\\Desktop\\FolderForPython\\
f.write("Here is a text from python.")
f.close()

# to append text:
f = open("tekstaDoku.txt","a")
f.write("\nHere is another text from python for second row.")
f.close()

# Read
f = open("tekstaDoku.txt","r") # "r"
for line in f:
    print(line.strip()) # strip - bez jaunam linijam
    # tokens = line.split(' ')
    # print(str(tokens), len(tokens))
f.close()

f = open("tekstaDoku.txt","r")
f_toPrint = open("tekstaDokuToPrint.txt","w")

for line in f:
    tokens = line.split(' ')
    f_toPrint.write("Wordcount: "+str(len(tokens))+". "+line)

f.close()
f_toPrint.close()

# 2.punktam "find and print them out selectively"
# izprintēt tos ierakstus, kuri satur tekstu "2024"
print("\nSecond task:")
f = open("textDoc_1.txt", "w")
f.write("2024-01-06,10:00:01,ERROR,Connection failed on server1")
f.write("\n2025-02-06,10:01:01,ERROR,Connection failed on server2")
f.write("\n2024-02-08,10:02:01,ERROR,Connection failed on server3")
f.close()
f = open("textDoc_1.txt","r")
keyword="2024"
for line in f:
    tokens = line.split(' ')
    for x in tokens:
        if keyword in x:
            print(line.strip())
f.close()

# 3.p filter out fields within the log line
print("\nThird task:")
try:
    f = open("textDoc_1.txt", "r")
    try: 
        f_output = open("logsWithFilteredFields.txt", "w")
        for line in f:
            fields = line.split(',')
            date = fields[0]
            time = fields[1]
            log_level = fields[2]
            message = fields[3]
            print(("Date: {}, Time: {}, Log Level: {}, Message: {}".format(date,time,log_level, message)).strip()) # print in console
            f_output.write(f"Date: {date}, Time: {time}, Log Level: {log_level}, Message: {message}") # print in other file
        f_output.close()

    except FileNotFoundError:
        print("This file was not found!")
    f.close()
except FileNotFoundError:
    print("This file was not found!")
