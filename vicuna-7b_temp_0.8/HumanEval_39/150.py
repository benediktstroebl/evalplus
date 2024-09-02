

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

    if n % 2 == 0:
        return 0

    a, b = 1, 1
    for i in range(2, n - 1):
        if (a ** 2 + b ** 2 > n):
            a, b = b, a + b
        else:
            a = b + a
    return a