

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
    if n == 0 or n == 1:
        return n
    p0 = 0
    p1 = 1
    counter = 2
    while(p1 < n):
        p0, p1 = p1, p1 + p0
        counter += 1
        if isPrime(counter):
            print(counter,p1)
            if p1 == n:
                return counter
    return -1
