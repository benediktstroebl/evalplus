

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
    a, b, p = 1, 1, 1
    while not (a % 2 and a % 3 and a % 5 and a % 7 and a % 11 and a % 13):
        a, b = b, b + a
        p += 1
    if p >= n:
        return a
    for i in range(n - p):
        a, b = b, b + a
    return a

