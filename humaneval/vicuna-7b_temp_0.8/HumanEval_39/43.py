

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
    if n < 2:
        return 2
    if n <= 1:
        return 1
    if n in [2, 3]:
        return n
    for i in range(2, n):
        for j in range(i, n):
            if (j - 1) % i == 0:
                return 0
        if (i - 1) % j == 0:
            return 0
    return 1
