

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
    if n < 4:
        return n
    if n % 2 == 0:
        return 1
    if n % 3 == 0:
        return 3
    d = 5
    while d * d <= n:
        if d % 2 == 0:
            d += 1
        else:
            d *= 3
    return d
