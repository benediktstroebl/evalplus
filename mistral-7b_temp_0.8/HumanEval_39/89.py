

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
    assert n >= 1
    n -= 1
    p = 0
    m = 1
    while m <= n:
        t = p
        p = m
        m = t + m
        if m % 2 == 0:
            p -= 1
            m -= 1
            p %= m
            while m >= p:
                m -= p
                m %= p
    return p

