n=(int(input("ile liczb: ")))
sum=0
i=0
for i in range(n):
    x=int(input("next number: "))
    sum=x+sum
    
avg=sum/n
print(avg)