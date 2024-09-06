

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

    from math import sqrt
    from itertools import count, islice
    n = n - 1
    f = next(islice(count(2), n, None))
    a = f
    b = f + 1
    while True:
        if b > n:
            raise IndexError("Index is too big.")
        if not (b % 2):
            b += 1
            continue
        if not is_prime(b):
            b += 1
            continue
        if (a + b) > n:
            return b
        a, b = b, a + b

