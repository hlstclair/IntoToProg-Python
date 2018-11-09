'''
=======================================
Developer: Hilde St.Clair
Date: 11-06-2018
Assignment: Module 05
Description: Read from text file,
load data into a dictionary,
allow users to add/remove from choices
=======================================
'''


# 1. Create a text file, with the data, Clean House,low and Pay Bills,high
newFile = open("Todo.txt", "w")
newFile.write("Clean House,low\n")
newFile.write("Pay Bills,high")


# 2. When the program starts, load each row of data from the text file into a Python dictionary.
# (The data will be stored like a row in a table.)
# 3. After you get the data in a Python dictionary, Add the new dictionary “row”
# into a Python list object (now the data will be managed as a table).

newFile = open("Todo.txt", "r")
#print(newFile.read())
# testing
fileData = ""
fileRow = {}
fileTable = []

for line in newFile:
    fileData = line.split(",")  #divide the data into two elements
    #print(fileData) #testing
    #print(fileData[0].strip())
    #print(fileData[1].strip())
    fileRow = {"Task": fileData[0].strip(), "Priority": fileData[1].strip()}
    fileTable.append(fileRow) #append!
print(fileTable)
# testing
newFile.close()

# 4. Display the contents of the List to the user.
print(fileTable)

# 5.Allow the user to Add or Remove tasks from the list using numbered choices:
while(True):
    print("""
        Menu of Options
        1)  Show current data
        2)  Add a new item.
        3)  Remove an existing item.
        4)  Save Data to File
        5)  Exit Program
        """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("The current items to do are:")
        for row in fileTable:
            print(row["Task"] + "-" + row["Priority"] + ".")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        #for row in fileTable:
        newTask = str(input("What is the task? ")).strip()
        newPriority = str(input("What is the priority? high/low ")).strip()
        fileRow = {"Task": newTask, "Priority": newPriority}
        fileTable.append(fileRow)
        print("Current items in list:")
        for fileRow in fileTable:
            print(fileRow)
        print("The new To Do List is: ")
        for row in fileTable:
            print(row["Task"] + "-" + row["Priority"] + ".")
            #print(fileTable)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        removeTask = input("Which task would you like to remove from the list? ")
        flagRemove = False
        taskNumber = 0
        while(taskNumber < len(fileTable)):
            if removeTask == str(list(dict(fileTable[taskNumber]).values())[0]):
                del fileTable[taskNumber]
                flagRemove = True
            taskNumber += 1
        if(flagRemove == True):
            print("The task was removed.")
        else:
            print("Sorry, I could not find that task.")
        print("The current items in the list are: ")
        for row in fileTable:
            print(row["Task"] + "-" + row["Priority"] + ".")
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        print("The current To Do items are: ")
        for row in fileTable:
            print(row["Task"] + "-" + row["Priority"] + ".")
            if ("y" == str(input("Do you want to save this file? y/n")).strip().lower()):
                file = open("Todo.txt", "w")
                for fileRow in fileTable:
                    file.write(fileRow["Task"] + "," + fileRow["Priority"])
                file.close()
                input("Data has been saved. Press enter to return to menu.")
            else:
                input("Data unable to save. Press enter to return to menu.")
                for row in fileTable:
                    print(row["Task"] + "-" + row["Priority"] + ".")
            continue
    elif (strChoice == '5'):
        break  # and Exit the program