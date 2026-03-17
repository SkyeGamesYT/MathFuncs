from Sections import *
from consolemenu import *
from consolemenu.items import *
import os

menu = ConsoleMenu("Math Helper")
#os.system("clear")

def CalculateMMR():
    #os.system("clear")
    canContinueMMR = True
    numListMMR = []

    while canContinueMMR:
        ans = input("Please input a whole number OR input X to exit continue: ")
        if ans.lower() != "x":
            ans = int(ans)

            numListMMR.append(ans)
        else:
            canContinueMMR = False

    mea = meanCalc.get_mean_from_list(numListMMR)
    med = medianCalc.get_median_from_list(numListMMR)
    ran = rangeCalc.get_range_from_list(numListMMR)
    stdev = standardCalc.get_stdev_from_list(numListMMR)

    os.system("clear")  # or "cls" on Windows

    print("=== Results ===")
    print(f"Mean: {mea}")
    print(f"Median: {med}")
    print(f"Range: {ran}")
    print(f"Standard Deviation: {stdev}")
    input("\nPress Enter to return...") 



def calculateSqRt():
    os.system("clear")

    question = input("Please enter the number you'd like to Square Root: ")

    if int(question) >= 0:
        regSqRoot.regular_sqrt(int(question))
    else:
        advSqRt.advanced_sqrt(float(question))
        






MMR = FunctionItem("Mean, Median, Range Calculator", CalculateMMR)


menu.append_item(MMR)


menu.show()