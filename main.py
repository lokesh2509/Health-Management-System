# # Health Management System
# # Total 6 Files, 3 For exercise and 3 For for diet
# # 3 clients - Ansh, Pranav and Shlok
# # write a function that when executed takes as input client name
# # one more function to retrieve exercise or food for any client


import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("Ansh_Exercise.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("Ansh_Food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Pranav_Exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Pranav_Food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Shlok_Exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Shlok_Food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Ansh),2(Pranav),3(Shlok)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("Ansh_Exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("Ansh_Food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Pranav_Exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Pranav_Food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Shlok_Exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Shlok_Food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Ansh,Pranav,Shlok)")
print("health management system: ")
a=int(input("press 1 for lock the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for Ansh\n 2 for Pranav\n 3 for Shlok "))
    take(b)
else:
    b = int(input("press 1 for Ansh\n 2 for Pranav\n 3 for Shlok "))
    retrieve(b)