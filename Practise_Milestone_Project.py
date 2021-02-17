# MILESSTONE - PROJECT-1 

#DISPLAYING INFO LIKE STRUCTURE OF TIC TIK TAC GAME
#LIKE THIS
# [1,2,3]
# [4,5,6]
# [7,8,9]

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']

display(row1,row2,row3)

#row2[1]='X'
#display(row1,row2,row3)
## ACCEPT USER INPUT 

#user=int(input("Choose the Value"))
#row1[user]
#print(row1[user])
#row2[1]
#print(row2)

#METHOD CHECK USER 1
def check():
    user=0
    while True:
        try:
            user=int(input("Enter Value: "))
        except  ValueError:
            print("This is Not a Number !")
            continue
        else:
            print("Yes Done")
            break
#METHOD CHECK USER 2
def user_ck():
    user=input("Enter th value")
    if user.isdigit():
        print("DONE K")
    else:
        print("No Done")

#METHOD CHECK USER 3
def user_c():
    choice='WRONG'
    while choice.isdigit()==False:
        choice=input("Enter the Value: ")
        if choice.isdigit()==False:
            print("OOPs! Plz Enter Valid Value in integer")
    return int(choice)


def user_c():
    #VARIABLES

    #INITIAL
    choice='WRONG'
    accepta_range=range(0,10)
    withinrange=False

    while choice.isdigit()==False or withinrange==False:
        choice=input("Enter the Value: ")

        #DIGIT CHECK
        if choice.isdigit()==False:
            print("OOPs! Plz Enter Valid Value in integer")
        
        #RANGE CHECK
        if choice.isdigit()==True:
            if int(choice) in accepta_range:
                withinrange=True
            else:
                withinrange=False
                print("PLz! Enter a Value within range. ")
    return int(choice)
user_c()



