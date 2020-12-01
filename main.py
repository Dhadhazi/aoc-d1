with open("d1-reportrepair") as file:
    lines = file.read().splitlines()

numbers = []

for line in lines:
    numbers.append(int(line))

#Brute force solutions
num1 = 0
num2 = 0

for i in range(0, len(numbers)-1):
    if num1 != 0:
        break
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            num1 = numbers[i]
            num2 = numbers[j]
            break

print(f"part one solution: {num1*num2}")

num1 = 0
num2 = 0
num3 = 0

for i in range(0, len(numbers)-1):
    if num1 != 0:
        break
    for j in range(i+1, len(numbers)):
        if num1 != 0:
            break
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                num1 = numbers[i]
                num2 = numbers[j]
                num3 = numbers[k]
                break

print(f"part two solution: {num1*num2*num3}")