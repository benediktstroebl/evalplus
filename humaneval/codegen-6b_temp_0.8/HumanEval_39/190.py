

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
    if n == 0 or n == 1:
        return n
    if n == 2:
        return 3
    if n == 3:
        return 5

    fib_1, fib_2 = 1, 2
    for scalar in range(3, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2
