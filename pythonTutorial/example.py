
for n in range(2, 10):
    for x in range(2,n):
        if n % x == 0:
            print (n, 'equals', x, '*', n//x)
            break
    else: #Interesting that i can use an 'else' without an 'if'
        print(n, 'is a prime number')

        
