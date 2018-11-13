'''
=========================================
Developer: Hilde St.Clair
Date: 11-12-2018
Assignment: Module 06
Description: Place the code you created
for working with your ToDo.txt file into
Functions and a Class.
=========================================
'''

newFile = open("Todo.txt", "w")
newFile.write("Clean House,low\n")
newFile.write("Pay Bills,high")

newFile = open("Todo.txt", "r")
#print(newFile.read())
# testing
fileData = ""
fileRow = {}
fileTable = []

class IO:
    @staticmethod
    def OutputMenuItems():
        '''Display the menu of choices'''
        print("""
                Menu of Options
                1)  Show current data
                2)  Add a new item.
                3)  Remove an existing item.
                4)  Save Data to File
                5)  Exit Program
                """)
    # end of function

    @staticmethod
    def InputMenuChoice():
        '''List what the menu of options are for the  user to call on'''
        strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
        return strChoice
    # end function

    @staticmethod
    def InputTasktoAdd():
        '''# Ask what task the user wants to add, return (task, priority)'''
        newTask = str(input("What is the task? ")).strip()
        newPriority = str(input("What is the priority? high/low ")).strip()
        return newTask, newPriority
    # end function

    @staticmethod
    def InputTasktoDelete():
        '''Ask what task the user wants to delete'''
        return str(input("Which task would you like to remove from the list? ")).strip()
    # end function

    @staticmethod
    def InputSavetoFile():
        '''Ask the user if they want to save'''
        return str(input("Do you want to save this file? y/n")).strip().lower()
    # end function

    @staticmethod
    def CurrentTasks(fileTable):
        '''Show items in the tasks table'''
        for row in fileTable:
            print(row["Task"] + "-" + row["Priority"] + ".")
    # end function

    @staticmethod
    def AdditionStatus(ItemAdded):
        '''Was the new task added'''
        if (ItemAdded) == (True): print("The task was added.")
        else:
            print("Sorry the program could not add your item. Try again later.")
    # end function

    @staticmethod
    def DeleteStatus(ItemRemoved):
        '''Was the task removed'''
        if (ItemRemoved) == (True): print("The item was successfully removed.")
        else:
            print("Sorry the program cannot remove that currently. Try again later.")
    # end function

# end class


class DataProcessor:
    @staticmethod
    def GetDatafromFile(newFile, fileTable):
        '''Pull data from Todo.txt file into a dictionary'''
        for line in newFile:
            fileData = line.split(",")  # divide the data into two elements
            # print(fileData) #testing
            # print(fileData[0].strip())
            # print(fileData[1].strip())
            fileRow = {"Task": fileData[0].strip(), "Priority": fileData[1].strip()}
            fileTable.append(fileRow)  # append!
        print(fileTable)
        # testing
        newFile.close()
    # end function

    @staticmethod
    def InsertTask(Task, Priority, fileTable):
        '''Add new item to the list'''
        fileRow = {"Task": newTask, "Priority": newPriority}
        fileTable.append(fileRow)
    # end function

    @staticmethod
    def DeleteTask(KeytoRemove, fileTable):
        '''Ask which item the user would like to remove'''
        flagRemove = False
        taskNumber = 0
        while (taskNumber < len(fileTable)):
            if removeTask == str(list(dict(fileTable[taskNumber]).values())[0]):
                del fileTable[taskNumber]
                flagRemove = True
            taskNumber += 1
        return flagRemove
    # end function

    @staticmethod
    def InsertData(newFile, fileTable):
        newFile = open("Todo.txt", "w")
        for line in newFile:
            newfile.write(fileRow["Task"] + "," + fileRow["Priority"] + "\n")
        newfile.close()
    # end function
# end class

DataProcessor.GetDatafromFile(newFile, fileTable)
while(True):
    IO.OutputMenuItems()
    strChoice = IO.InputMenuChoice().strip()

    if (strChoice) == ("1"):
        IO.CurrentTasks(fileTable)
        continue
    elif (strChoice) == ("2"):
        Task, Priority = IO.InputTasktoAdd()
        DataProcessor.InsertTask(Task, Priority, fileTable)
        IO.CurrentTasks(fileTable)
        continue
    elif (strChoice) == ("3"):
        KeytoRemove == IO.InputTasktoDelete()
        blnStatus = DataProcessor.DeleteTask(KeytoRemove, fileTable)
        IO.DeleteStatus(blnStatus)
        IO.CurrentTasks(fileTable)
        continue

    elif(strChoice) == ("4"):
        IO.CurrentTasks(fileTable)
        if("y" == IO.InputSavetoFile()):
            DataProcessor.InsertData(newFile, fileTable)
        else:
            pass
        continue

    elif(strChoice) == ("5"):
        break
