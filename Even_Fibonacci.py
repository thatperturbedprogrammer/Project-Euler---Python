#Fibonacci Series
n1 = 0
n2 = 1
fiblist = []
count = 0

print("10 Fibonacci Number Series:")
while(count < 10):
    print(n1, end=",")
    fiblist.append(n1)
    n3 = n1+n2
    n1 = n2
    n2 = n3
    count += 1

print()

#Even Fibonacci Sum
even_fib_sum = 0
for i in fiblist:
    if(i%2 == 0):
        even_fib_sum += i

print("Sum of Even Fibonacci Numbers: ", even_fib_sum)
