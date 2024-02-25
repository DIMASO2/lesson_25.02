"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 80]
result = []
for number in numbers:
    if number > 5 and number < 50:
        result.append(number)
print(result)

result = filter(lambda number:number > 5 and number < 50, numbers)
print(list(result))

boba = [1, 3, 5, 7, 9]
result = [biba for biba in boba if biba > 1 and biba < 9]
print(result)

names = ["man", "ban", "can", "dig", "mag"]
NAMES = []
for name in names:
    if name[0] == "m":
        NAMES.append(name.upper())
print(NAMES)

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kosips = []
for sp in spisok:
    if sp < 5: kosips.append(0)
    else: kosips.append(1)
print(kosips)
"""

result = {i:i**2 for i in range(1, 10)}
print(result)