

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
    a = 2
    b = 3
    while True:
        c = (a+b) % MOD
        if c!= 1 and c!= 0:
            return c
        a = b
        b = c
    return c
