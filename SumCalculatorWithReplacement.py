newNumEnt = False
newNum = ""
total = 0
print("Enter a string of single digit numbers with no spaces: ")
nums = input()
for i in range(0, len(nums) - 1 + 1, 1):
    index = nums[i]
    codeNum = ord(index)
    while codeNum < 48 or codeNum > 57:
        print("Invalid input for index " + str(i) + "! Please enter a new value to take its place: ")
        newNum = input()
        codeNum = ord(newNum)
        newNumEnt = True
    if newNumEnt == True:
        newChar = chr(codeNum)
        intIndex = int(newChar)
        total = total + intIndex
    else:
        intIndex = int(index)
        total = total + intIndex
print("The sum of the numbers entered is: " + str(total))
