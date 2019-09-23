#1
#vul een nummer in en dan kijk hij eerst of het een positief getal of negatief getal is
number = int(input("Enter a number"))
if number == 0:
    print("The number is zero")
if number > 0:
    print("The number is positive")
if number < 0:
    print("The number is negative")
#hier kijkt hij of het een even of oneven getal is door het gebruiken van een som die ik heb gevonden op het internet
if (number % 2) == 0:
    print("{0} is Even number".format(number))
else:
    print("{0} is Odd number".format(number))
print("--------------------------------------------------------------------------------------------")
#2
    #Invoegen van de nummers hier
RecLo = int(input("Enter the lenght of your first rectangle"))
RecWo = int(input("Enter the width of your first rectangle"))
RecLs = int(input("Enter the lenght of your second rectangle"))
RecWs = int(input("Enter the width of your second rectangle"))
Reco = int(RecLo) + int(RecWo)
Recs = int(RecLs) + int(RecWs)
#Print welke groter is of als ze gelijk zijn
if Reco > Recs:
    print("The first rectangle is bigger")
elif Reco < Recs:
    print("The second rectangle is bigger")
if Reco == Recs:
    print("The rectangles are the same size")
print("--------------------------------------------------------------------------------------------")
#3
#De code kijkt eerst of het getal tussen de 0-36 zit als die dat niet is dan gaat hij niet verder
Pnumber= int(input("Enter a pocket number"))
if Pnumber < 0 or Pnumber > 36:
    print("Error, please enter a number between 0 and 36")
else:
    if Pnumber == 0:
        print("The pocket is green")
    elif Pnumber < 11:
        #met / 2 als kijk je of het getal een even of oneven getal is als dit het niet is print die dat het rood is
        #als die wel even is print die dat het zwart is dat doet hij bij elke nummer stap
        if Pnumber / 2 !=0:
            print("The pocket is red")
        else:
            print("The pocket is black")
    elif Pnumber < 19:
        if Pnumber / 2 !=0:
            print("The pocket is red")
        else:
            print("The pocket is black")
    elif Pnumber < 29:
        if Pnumber / 2 !=0:
            print("The pocket is red")
        else:
            print("The pocket is black")
print("--------------------------------------------------------------------------------------------")
#4
#Beantwoord de vragen als er geen ja of nee word ingevoerd dan geeft het het aan.
print("You apear to be having some wifi trouble")
print("Reboot the computer and try to connect")
X = input("Did that fix the problem")
if X == "Yes":
    print("The problem is fixed")        
if X == "No":
    print("Reboot the router and try to connect")
else:
    print("please enter Yes or No")
X = input("Did that fix the problem")
if X == "Yes":
    print("The problem is fixed")
if X == "No":
    print("Make sure the cables between the router and modum are plugged in firmly")
else:
    print("please enter Yes or No")
X = input("Did that fix the problem")
if X == "Yes":
    print("The problem is fixed")
if X == "No":
    print("Move the router to a new location")
else:
    print("please enter Yes or No")
X = input("Did that fix the problem")
if X == "Yes":
    print("The problem is fixed")
if X == "No":
    print("Get a new router")
else:
    print("please enter Yes or No")

print("--------------------------------------------------------------------------------------------")
#5                                                          #Lijst wat je bij elk rest kan eten
Rest1 = "Joe's Gourmet Burgers"                             #Not Veg, Not Vegan , Not Gluten-Free
Rest2 = "Main Street Pizza Company"                         #Yes veg, Not Vegan , Yes Gluten-Free
Rest3 = "Corner Cafe"                                       #Yes veg, Yes Vegan , Yes Gluten-Free
Rest4 = "Mama's Fine Italian"                               #Yes veg, Not Vegan , Not Gluten-Free
Rest5 = "The Chef's Kitchen"                                #Yes veg, Yes Vegan , Yes Gluten-Free
opties = "Here are your restaurant choices:"

print("Hello Welcome to the Restaurant Selection App")
vegi = str(input("Enter yes if any of your guests is vegetarian:"))       #hier kijk je of iemand vegi, vegan of gluten mag eten
vegan = str(input("Enter yes if any of your guests are vegan:"))          
gluten = str(input("Enter yes if any of your guests eat gluten-free:"))    
print()
                                                                           #Lijst voor wat je wel en niet kan bij deze opties
if vegi=='yes' and vegan=='yes' and gluten=='yes':                         #Yes veg, Yes Vegan , Yes Gluten-Free
  print(opties,'\n',Rest3,'\n',Rest5)                                      
  
elif vegi=='yes' and vegan=='yes' and gluten=='no':                        #Yes veg, Yes Vegan , No Gluten-Free
  print(opties,'\n',Rest3,'\n',Rest5)                                      
    
elif vegi=='yes' and vegan=='no' and gluten=='yes':                        #Yes veg, No Vegan , Yes Gluten-Free
  print(opties,'\n',Rest2,'\n',Rest3,'\n',Rest5)                           
    
elif vegi=='no' and vegan=='yes' and gluten=='yes':                        #No veg, Yes Vegan , Yes Gluten-Free
  print(opties,'\n',Rest3,'\n',Rest5)                                      
  
elif vegi=='no' and vegan=='yes' and gluten=='no':                         #No veg, Yes Vegan , No Gluten-Free
  print(opties,'\n',Rest3,'\n',Rest5)                                      
  
elif vegi=='no' and vegan=='no' and gluten=='yes':                         #No veg, No Vegan , Yes Gluten-Free
  print(opties,'\n',Rest2,'\n',Rest3,'\n',Rest5)                           
  
elif vegi=='yes' and vegan=='no' and gluten=='no':                         #Yes veg, No Vegan , No Gluten-Free
  print(opties,'\n',Rest2,'\n',Rest3,'\n',Rest4,'\n',Rest5)                
  
elif vegi=='no' and vegan=='no' and gluten=='no':                          #No veg, No Vegan , No Gluten-Free
  print(opties,'\n',Rest1,'\n',Rest2,'\n',Rest3,'\n',Rest4,'\n',Rest5)     





