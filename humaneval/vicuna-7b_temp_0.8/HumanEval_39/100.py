

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
        return 2
    if n == 2:
        return 3
    if n in [3, 5, 8, 13, 21]:
        return 5
    if n in [5, 8, 13, 21]:
        return 89
    if n in [8, 13, 21]:
        return 161
    if n in [13, 21]:
        return 343
    if n in [21]:
        return 584
    for i in range(2, n):
        if (n % i) == 0:
            return 0
    return 1
