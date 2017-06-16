def fun(n):
    """Recursive function to
        print Fibonacci sequence"""
if n <= 1:
    return n
else:
    return(fun(n-1) + fun(n-2))

# receive input from the user
terms = int(input("How many terms U want Fibonacci ?: "))

if terms <= 0:
    print("Plese enter only positive integer")
else:
    print("Fibonacci Series:")
        for i in range(terms):
            print(fun(i))