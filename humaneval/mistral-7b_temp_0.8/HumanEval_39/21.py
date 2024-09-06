

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
    a, b, c = 0, 1, 1
    for i in range(2, n):
        if (b ** 2 - 4 * a * c) ** 0.5 % 2 == 0:
            a, b, c = b, c + a + b, a
        else:
            a, b, c = c, a + b + c, b
        if c % 2 == 0:
            return prime_fib(i - 1)
    return c

