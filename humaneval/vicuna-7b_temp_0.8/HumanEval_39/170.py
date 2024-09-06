

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
        return 2
    if n < 3:
        return 3
    a, b = 0, 1
    for i in range(n-1, 0, -1):
        if (a * a + b * b) % i == 0:
            return i
        a, b = b, a + b
    return 2