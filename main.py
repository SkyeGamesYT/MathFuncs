from Sections import mean, median
import os

numList = []
canContinue = True

os.system("clear")


while canContinue:
    ans = input("Please input number OR input X to exit continue: ")
    if ans.lower() != "x":
        ans = int(ans)

        numList.append(ans)
    else:
        canContinue = False

mea = mean.get_mean_from_list(numList)
med = median.get_median_from_list(numList)

print("Mean: " + str(mea))
print("Median: " + str(med))


os.exit(1)


