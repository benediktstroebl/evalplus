

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
    a, b = 2, 3
    while True:
        c = a + b
        if c % 2 == 0:
            a, b = b, c
        else:
            a, b = c, b
        if is_prime(c):
            return c

