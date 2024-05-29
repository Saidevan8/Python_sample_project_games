#FUNCTION USED FOR THE PRINTING TIC-TAC-TOE BOXES
def printlist(l):
    for i in range(len(l)):
        for j in range(2):
            print(" ",l[i][j],end=" |")
        print(" ",l[i][2])
        if(i<2):
            print("----+----+----")
#FUNCTION USED FOR CHECKING FOR THE WINNER OR Tie 
def condition(l):
    if(l[0][0]==l[0][1] and l[0][0]==l[0][2] and l[0][1]==l[0][2] and l[0][0]!=" "):#row 1
        k=l[0][0]+"Won the match"
        print(k)
        return True
    elif(l[1][0]==l[1][1] and l[1][1]==l[1][2] and l[1][0]==l[1][2] and l[1][0]!=" "):#row 2
        k=l[1][2]+"--Won the match"
        print(k)
        return True
    elif(l[2][0]==l[2][1] and l[2][1]==l[2][2] and l[2][0]==l[2][2] and l[2][0]!=" "):#row 3
        k=l[2][0]+"--Won the match"
        print(k)
        return True
    elif(l[0][0]==l[1][0] and l[1][0]==l[2][0] and l[0][0]==l[2][0] and l[0][0]!=" "):#col 1
        k=l[0][0]+"--Won the match"
        print(k)
        return True
    elif(l[0][1]==l[1][1] and l[1][1]==l[2][1] and l[0][1]==l[2][1] and l[2][1]!=" "):#col2
        k=l[1][1]+"--Won the match"
        print(k)
        return True
    elif(l[0][2]==l[2][2] and l[2][2]==l[1][2] and l[1][2]==l[0][2] and l[0][2]!=" "):#col3
        k=l[2][2]+"--Won the match"
        print(k)
        return True
    elif(l[0][0]==l[1][1] and l[1][1]==l[2][2] and l[0][0]==l[2][2] and l[2][2]!=" "):#diag1
        k=l[0][0]+"--Won the match"
        print(k)
        return True
    elif(l[2][0]==l[1][1] and l[1][1]==l[0][2] and l[2][0]==l[0][2] and l[2][0]!=" "):#diag2
        k=l[2][0]+"--Won the match"
        print(k)
        return True
    else:
        return False
#FUNCTION FOR THE BOX IS EMPTY OR NOT
def check_space(a,b):
    if(l[a][b]=='O' or l[a][b]=='X'):
        return False
    return True
#MAIN PROGRAM
def main(l):
    printlist(l)
    i=0
    try:
        while(i<9):
            if(i%2==0):
                k=int(input("X turn to choose[0,1,2],[3,4,5],[6,7,8]:"))
                if(k<3 and k>=0):
                    if(check_space(0,k)):
                        l[0][k]="X"
                        i+=1
                    else:
                        print("Space is already filled")
                    printlist(l)
                elif(k>=3 and k<=5):
                    if(check_space(1,k%3)):
                        l[1][k%3]="X"
                        i+=1
                    else:
                        print("Space is already filled")
                    printlist(l)
                elif(k>=6 and k<=8):
                    if(check_space(2,k%3)):
                        l[2][k%3]="X"
                        i+=1
                    else:
                        print("Space is already filled")
                    printlist(l)
                else:
                    print("INVALID INPUT")
            else:
                k=int(input("O turn to choose[0,1,2],[3,4,5],[6,7,8]:"))
                if(k<3 and k>=0):
                    if(check_space(0,k)):
                        l[0][k]="O"
                        i+=1
                    else:
                        print("Space is already filled")
                    printlist(l)
                elif(k>=3 and k<=5):
                    if(check_space(1,k%3)):
                        l[1][k%3]="O"
                        i+=1
                    else:
                        print("Space is already filled")
                    printlist(l)
                elif(k>=6 and k<=8):
                    if(check_space(2,k%3)):
                        l[2][k%3]="O"
                        i+=1
                    else:
                        print("Space is already filled")
                    printlist(l)
                else:
                    print("INVALID INPUT")
            if(i>=4):
                c=condition(l)
                if(c==True):
                    break
                else:
                    pass
            if(i==9):
                c=condition(l)
                if(c==False):
                    print("DRAW")
    except:
        print("INVALID INPUT PLEASE RESTART THE GAME")
choice='y'
while(choice=='y' or choice=='Y'):
    print("********** TIC-TAC-TOE **********")
    #CREATING EMPTY LIST FOR THE TIC-TAC-TOE GAME
    l=[[" "," "," "],[" "," "," "],[" "," "," "]]
    main(l)
    choice=input("Do you want to play again(y/n):")
print("ENJOY THE GAME")
