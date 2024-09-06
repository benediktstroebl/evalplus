

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
    fib_1 = 1
    fib_2 = 2

    if n < 3:
        return fib_1
    
    for i in range(2, n + 1):
        fib = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib
        if not is_prime(fib):
            return fib
    
    return
