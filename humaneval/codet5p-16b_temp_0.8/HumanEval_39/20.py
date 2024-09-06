

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
    fib_1, fib_2 = 1, 1
    i = 2
    while i <= n:
        fib_1, fib_2 = fib_1 + fib_2, fib_1
        if (not (fib_1 > 4000000)) and (fib_1 % 2 == 0 or fib_1 % 3 == 0 or fib_1 % 5 == 0 or fib_1 % 7 == 0):
            i += 1
    return fib_2

