import csv 
import math
with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    file = list(reader)

data = file[0]
#step 1 finding mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean
#step 2 squaring values
square_list = []
for n in data:
    a = int(n)-mean(data)
    a = a ** 2
    square_list.append(a)
#step 3 claculate sum

sum = 0 
for i in square_list:
    sum = sum+i

#step 4 dividing sum by total values
result = sum/(len(data)-1)

#step 5 getting standard deviation by square root
sd = math.sqrt(result)
print(sd)