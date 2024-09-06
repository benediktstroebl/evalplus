

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
    fib, fib_2 = 0, 1
    while fib < n:
        if fib % 2 == 0:
            fib_2, fib = fib, fib_2 + fib
        else:
            fib_2, fib = fib, fib_2 + fib
    return fib
