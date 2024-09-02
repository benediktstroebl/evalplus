

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
    fib1 = 1
    fib2 = 2
    i = 3
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2
        i += 1
    if i == n:
        return fib2
    elif i < n:
        return fib2, i
