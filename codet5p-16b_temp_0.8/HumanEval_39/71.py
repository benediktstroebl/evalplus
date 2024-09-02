

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

    a, b = 0, 1
    while a + b < n:
        a, b = b, a + b
    return b if (n > 2 and not (a > 1 and all(a % x for x in range(2, a)))) else 0

