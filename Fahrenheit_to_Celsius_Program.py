#Caiya Mimms | Jan 21,2023
#Fahrenheit_to_Celsius_Program | HW #1
#Converts degrees of Fahrenheit to Celsius(User Input) 

print("Welcome! This program converts Fahrenheit to Celsius.")
    #Input
F = input ("Enter degrees in Fahrenheit: ")

    #Turning F to a float and converting to c
F = float(F)
C = (F-32) * (5/9)

    #Round off decimal to the 2nd place
rn_C =round(C*100.00)/100.00

    #Output(s)
print (rn_C,"C")
print ("Program End.")

    #Note: Python does not like the "dot" used to write temp. lesson learned.
