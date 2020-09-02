def collatz(num):
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3
        num += 1
    return num

num = int(input('Enter number: \n'))
newNum = collatz(num)
while True:
    print(newNum)
    if newNum == 1:
        break
    newNum = collatz(newNum)
