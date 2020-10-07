import random

def game(comp,you):
    if comp == you:
        return None  #**
    elif comp=="r":
        if you=="s":
            return False
        elif comp=="r":
          if you=="p":
            return True   
    elif comp=="s":
        if you=="r":
            return True
        elif comp=="s": 
           if you=="p":
            return False
    elif comp=="p":
        if you=="s":
            return True
        elif comp=="p": 
          if you=="r":
            return False                                   


print("Computer's turn Rock(r) Paper(p) Scrissor(s)")
autom=random.randint(1,3)
if autom==1:
    comp="r"
elif autom==2:
    comp="p"
elif autom==3:
    comp="s"        

you=input("Your's turn Rock(r) Paper(p) Scrissor(s)")

show=game(comp,you)

print(f"computer choose {comp} ")
print(f"You choose {you} ")

if show == None:
    print("its a Draw")
elif show:
    print("you win")
else:
    print("you lose")        
