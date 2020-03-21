x = input("Select your input format F/C: ")

if x == "F" or x == "f":
    f = input("Enter temp in F: ")
    f = int(f)
    c = round((f-32)*(5/9),2)
    print("Temp for " + str(f) + " in C is: " + str(c))
elif x == "C" or x == "c":
    c = input("Enter temp in C: ")
    c = int(c)
    f = round(c*(9/5)+32,2)
    print("Temp for " + str(c) + " in F is: " + str(f))
else:
    print("Please enter valid input")