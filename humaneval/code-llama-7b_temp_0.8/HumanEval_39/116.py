

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

    fib_2 = 2
    fib_1 = 3
    fib_n = fib_1 + fib_2

    for i in range(3, n):
        fib_2 = fib_1
        fib_1 = fib_n
        fib_n = fib_1 + fib_2

    return fib_n

