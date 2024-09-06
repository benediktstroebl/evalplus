

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    #pre-defining variables to avoid self assignments inside the loop
    prime = None
    number = None
    #default value for the number to be returned
    result = 0
    #this condition is needed to avoid looping endlessly
    if n < 1:
        return result
    #the initial Fibonacci numbers
    a = 0
    b = 1
    #counter to keep track of the number of iterations
    count = 0
    #the loop continues until the n-th prime Fibonacci number is found
    while prime is None:
        #calculating the next Fibonacci number
        number = a + b
        #updating the Fibonacci numbers
        a, b = b, number
        #checking if the number is prime
        prime = True
        #checking numbers from 2 up to the square root of the number
        for i in range(2, int(number ** 0.5) + 1):
            #if the number is not prime then break the loop
            if number % i == 0:
                prime = False
                break
        #if the number is prime and it's the right iteration, it's returned
        if prime and count == n - 1:
            result = number
            break
        #the number of iterations is incremented
        count += 1
    return result
