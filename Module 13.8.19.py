people_num = int(input("Введите количество посетителей: "))
sum = 0
for i in range(people_num):
    age = int(input(f"Введите возраст {i+1} посетителя: "))
    if 18 <= age < 25:
        sum += 990
    if age >= 25:
        sum += 1390
if people_num >= 3:
    sum *= 0.9
print(sum)
