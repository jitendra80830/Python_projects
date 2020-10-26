#break 
sum=0
for i in range(5):
    value=int(input())
    if(value<0):
        continue
    sum=sum+value
print("sum=",sum)