

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
    if n < 2:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    d = 0
    a = 1
    b = 1
    for i in range(4, n + 1):
        d, a, b = b, a + b, (a + b) % 2
    for _ in range(n - 2):
        a, b = b, a + b
    return (a * (d - b) + b) % 2
