

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
    i = 1
    while prime(i) == False:
        i += 1
    prime = i

    j = 0
    while j < n:
        j += 1
        i = fib(j)
        while prime(i) == False:
            i += 1
        prime = i
    
    return prime
