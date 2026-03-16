from Sections import meanCalc, medianCalc, rangeCalc
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

    menu.screen.printf("Mean: " + str(mea))
    menu.screen.printf("Median: " + str(med))
    menu.screen.printf("Range: " + str(ran))








MMR = FunctionItem("Mean, Median, Range Calculator", CalculateMMR)


menu.append_item(MMR)


menu.show()