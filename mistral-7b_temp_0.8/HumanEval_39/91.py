

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
    f, p = 1, 1
    i = 1
    while True:
        if f % p == 0:
            p, f = p + f, f
            i += 1
        elif i == n:
            return f
        else:
            f, p = f + p, p

