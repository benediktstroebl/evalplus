

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
    if n == 1:
        return 2
    if n == 2:
        return 3
    a = 1
    b = 2
    c = 0
    while True:
        c = a + b
        if (
            (c % 2 == 0 and c != 2)
            or c % 3 == 0
            or c % 5 == 0
            or c % 7 == 0
            or c % 11 == 0
            or c % 13 == 0
            or c % 17 == 0
        ):
            a = b
            b = c
            continue
        for i in range(2, int(c ** 0.5) + 1):
            if c % i == 0:
                a = b
                b = c
                continue
        return c

