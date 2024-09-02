

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
    a, b, c, p = 1, 1, 0, 0
    while p < n:
        c = a + b
        if is_prime(c):
            p += 1
        a, b = b, c
    return c

