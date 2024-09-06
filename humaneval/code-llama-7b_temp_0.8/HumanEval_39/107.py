

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
    #first two numbers are prime and Fibonacci numbers
    if n == 1:
        return 2
    if n == 2:
        return 3
    #aproximates the nth Fibonacci number
    fib_approx = (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / 5 ** 0.5
    #the difference between nth Fibonacci number and the approximate is an integer (due to the nature of Fibonacci numbers)
    fib_approx = int(fib_approx)
    #Fibonacci numbers are always odd, so we don't check even numbers
    for i in range(fib_approx-2, 1, -2):
        #checks if the number is prime
        if not is_prime(i):
            continue
        #checks if the number is the nth Fibonacci number
        if is_fib(i):
            return i
        #if it is not the nth Fibonacci number, the nth Fibonacci number is bigger than this one, so we can return it
        elif i < fib_approx:
            return i
    #returns the last Fibonacci number
    return fib_approx

