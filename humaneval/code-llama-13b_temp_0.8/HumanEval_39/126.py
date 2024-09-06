

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
    if n < 0:
        return -1
    a, b, i = 1, 1, 1
    while i < n:
        a, b = b, a + b
        i += 1
    if is_prime(b):
        return b
    return -1

