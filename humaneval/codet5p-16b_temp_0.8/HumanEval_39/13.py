

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

    if n <= 1:
        return 2
    fib_1 = 1
    fib_2 = 1
    fib_3 = 0
    for _ in range(3, n + 1):
        fib_3 = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_3
        if fib_3 % 2 == 0:
            fib_3 = fib_3 + 2
        if fib_3 % 3 == 0:
            fib_3 = fib_3 + 4
        if fib_3 % 5 == 0:
            fib_3 = fib_3 + 6
        if fib_3 % 7 == 0:
            fib_3 = fib_3 + 8
        if fib_3 % 11 == 0:
            fib_3 = fib_3 + 14
        if fib_3 % 13 == 0:
            fib_3 = fib_3 + 18
    return fib_3

