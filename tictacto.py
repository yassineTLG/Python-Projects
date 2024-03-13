import random

player={"item":"x"}
computer={"item":"o"}

    


def CheckWin(f):
    for sl in [(f[0]==f[1]==f[2]),(f[0]==f[3]==f[6]),(f[0]==f[4]==f[8]),(f[3]==f[4]==f[5]), (f[6]==f[7]==f[8]),(f[4]==f[1]==f[7]),(f[8]==f[5]==f[2]),(f[6]==f[4]==f[2])]:
        if sl == True:
              return True

def PrintFormula(formula):
    f = formula
    print(f"""  
                {f[0]} | {f[1]} | {f[2]}
                {f[3]} | {f[4]} | {f[5]}
                {f[6]} | {f[7]} | {f[8]}

          """)
def ReadNumber():
    number =0
    while True:
        print("----------------------------------------")
        print('enter your position from 1 to 9')
        try:
            number = int(input("enter your position >>> "))
            if number < 10 and number > 0:
                break
            else:
                print("eroor only nums 1 to 9 allowd")
        except:
            ValueError
    return number; 
def ReadData(data,computer,player,counter,StackChoices):
    if counter % 2 == 0:
        print("player tourne---------------->> X")
        ReadDataPlayer(data,player,StackChoices)
    else:
        print("computer tourne ------------->> O")
        ReadDataComputer(data,computer,StackChoices)
def ReadDataPlayer(data,player,StackChoices):
    while True:
        
        data["position"]=ReadNumber()
        if data["position"] in StackChoices:
            print("this position is full")
        else:
            break
    StackChoices.append(data["position"])
    data["item"]=player["item"]
    return data

def ReadDataComputer(data,computer,StackChoices):
    while True:
        data["position"]=random.randint(1,9)
        if not data["position"] in StackChoices:
            break
            
    StackChoices.append(data["position"])
    data["item"]=computer["item"]  
    return data
    
def EditFormula(formula,data):
    position = data['position']
    position -= 1
    formula[position] = data["item"]
        
           
def main(player,computer):
    
    
    run = True
    PlayerScore=0
    ComputerScore=0
    print("<He---------> X <---------> O <---->GAME")
    
    while True:
        counter = 0
        StackChoices=[]
        formula =[1,2,3,4,5,6,7,8,9]
        while run:
            counter += 1
            if counter == 10:
                print("even game")
                break
            Data ={"position":0,"item":""}
            
            print(f"Score X :{PlayerScore} >>>---------------<<< Score O :{ComputerScore}")
            PrintFormula(formula)
            ReadData(Data,computer,player,counter,StackChoices)
            Item0 = Data["item"]
            EditFormula(formula,Data)
            win =CheckWin(formula)
            if win == True:
                print("*************WIN***************")
                if Item0 == "x":
                    print("The winner is the player")
                    PlayerScore += 1
                else:
                    print("The winner is the computer")
                    ComputerScore += 1
                run = False

        
        print("you wanna play again")
        answer = input("enter y to continue the game ")
        if answer == "y":
            run = True
        else:
            print(f"Score X :{PlayerScore} >>>---------------<<< Score O :{ComputerScore}")
            break
        

    print("you quit the game")   
   
 
main(player,computer)