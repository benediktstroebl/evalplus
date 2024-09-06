

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
    f = 0
    s = 1
    p = 2
    i = 3
    while p <= n:
        if p < 2:
            p = 2
        elif p == 2:
            p = 3
        elif p == 3:
            p = 5
        else:
            p = f + s
            f = s
            s = p
        i += 1
    return p

