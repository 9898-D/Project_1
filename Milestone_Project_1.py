# MILESSTONE - PROJECT-1 

# Diplay Mylist create Functions



def display_mylist(my_list):
    print("Here Your Current List")
    print(my_list)

#display_mylist(my_list)

# PROCESS_CHECK USER INPUT

def process_check():
    choice="WRONG"

    while choice not in ['0','1','2']:
        choice=input("Pick Up the Value: ")

        if choice not in  ['0','1','2']:
            print("Invalid Input! Plz Try Again")
    
    return int(choice)
#process_check()

# REPLACEMENT OF USER INPUT INTO LIST

def replacement(my_list,position):
    user=input("Enter the String Put on List: ")
    my_list[position]=user

    return my_list

#print(replacement(my_list,1))

# FUNC TO USER KEE PLAYING GAME OR NOT

def game_on():
    choice="WRONG"

    while choice not in ['Y','N']:
        choice=input("Keep Playing or Not (Y,N)")

        if choice not in ['Y','N']:
            print("INVALID INPUT PLz Enter Y or N")
    
    if choice=='Y':
        return True
    else:
        return False
#print(game_on())

# INTIALZE ALL FUNCTIONS 
game_o=True
my_list=[0,1,2]
while game_o:

    display_mylist(my_list)

    pos=process_check()

    cu_list=replacement(my_list,pos)

    display_mylist(cu_list)

    game_o=game_on()