# Odd Even number

a=int(input("Enter the integer:"))

if (a % 2 ==1):
     print(a,"is an odd number")
else:
    print(a,"is an even number")


# Sum Of Integers

a=int(input("Enter first interger:"))
b=int(input("Enter second integer:"))
t= 0
for i in range(a,b+1):
    t += i
print('The sum of interger from',a,'to',b,'is',t)



