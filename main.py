#test
# Initialization
Indicator = False

# Functions
def Compare(xVal, yVal, zVal):
    global Indicator
    if xVal == yVal or xVal == zVal or yVal == zVal:
        Indicator = True
    else:
        Indicator = False

def indicator():
    if Indicator == True:
        print("Yes! There is a same value!")
    else:
        print("No! They are all different value!")

# Main Program
print("Let's compare the values!")
print("Please insert any value to the following variables")
xVal = int(input("X = "))
yVal = int(input("Y = "))
zVal = int(input("Z = "))

Start = input("Whether any of the value are the same? Press Enter to compare!")
if Start == "":
    Compare(xVal, yVal, zVal)
    indicator()