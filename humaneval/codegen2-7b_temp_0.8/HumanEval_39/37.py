

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
    a, b, c = 2, 3, 5
    while n > 0:
        if is_prime(c):
            return c
        else:
            a, b, c = b, c, a + b
        n -= 1
