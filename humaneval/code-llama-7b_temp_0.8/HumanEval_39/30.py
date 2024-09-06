

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
        raise ValueError("n must be >= 1")

    fib1 = 1
    fib2 = 1
    fib = 2

    if n == 1:
        return fib1
    if n == 2:
        return fib2

    for i in range(2, n):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib

    return fib

