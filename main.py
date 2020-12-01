with open("d1-reportrepair") as file:
    lines = file.read().splitlines()

numbers = []

for line in lines:
    numbers.append(int(line))

#Hashmap one run, only for part one
map = {}

def find_sum_two(sum):
    for i, n in enumerate(numbers):
        diff = sum - n
        if diff in map:
            return [diff, n]
        map[n] = i

sum2 = find_sum_two(2020)
print(f"part one solution: {sum2[0]*sum2[1]}")

#Hashmap two run for both parts
hashed_map = {n:i for (i,n) in enumerate(numbers)}

def find_sum_two_in_map(target):
    for i in range(0, len(numbers)-1):
        if target-numbers[i] in hashed_map and i != hashed_map.get(target - numbers[i]):
            return [numbers[i], target-numbers[i]]
    return False

sum2 = find_sum_two_in_map(2020)
print(f"part one solution: {sum2[0]*sum2[1]}")


for i in range(0, len(numbers)-2):
    found_numbers = find_sum_two_in_map(2020-numbers[i])
    if found_numbers:
        print(f"part two solution: {numbers[i]*found_numbers[0]*found_numbers[1]}")
        break

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