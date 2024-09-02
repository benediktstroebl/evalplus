

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
    if n < 1:
        return n
    if n == 1:
        return 2
    if n == 2:
        return 3
    for i in range(5, n * n):
        a = i * i + 4 * i * (i - 2)
        b = i * i + 4 * i * (i - 1)
        c = i * i + 4 * i * (i - 1) + 2 * i
        d = i * i + 4 * i * (i - 1) + 4 * i * (i - 2)
        if a > n or b > n or c > n or d > n:
            return i - 1
    return i

