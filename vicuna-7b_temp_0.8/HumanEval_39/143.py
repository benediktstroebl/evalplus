

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
        return n
    if n <= 2:
        return 1
    if n % 2 == 0:
        return 1
    for i in range(3, n + 1, 2):
        if (n - i) % 2 == 0:
            return 1
    if (n - 2) % 2 == 0:
        return 1
    for i in range(3, int(n ** 0.5) + 1, 2):
        if (n - i) % 2 == 0:
            return 1
    return 1
