import math
import csv
with open("data.csv",newline="" ) as f :
    reader=csv.reader(f)
    data=list(reader)
data=data[0]
def mean(data):
    n= len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
squaredlist=[]
for num in data:
    a=int(num)-mean(data)
    a=a**2
    squaredlist.append(a)
sum=0
print(squaredlist)
for i in squaredlist:
    sum=sum+i
result=sum/(len(data)-1)
standardeviation=math.sqrt(result)
print(standardeviation)        