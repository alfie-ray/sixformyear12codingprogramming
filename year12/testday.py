import random
hello = 0
while hello != 5:
    num = random.randint(0, 100)
teams=["monday","tuesday","wednesday","thursday","friday"]
points=[num,num,num,num,num]
num = random.randint(0, 100)
hello = 0 + 1

for i in range(len(teams)):
    print(teams[i]+ ": " +str(points[i]))