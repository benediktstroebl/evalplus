

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
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer."
    if n == 0:
        return 1
    if n == 1:
        return 2
    a = 2
    b = 3
    f0 = 1
    f1 = 2
    for _ in range(n - 1):
        a, b = b, a + b
        f0, f1 = f1, a
    if isPrime(f0):
        return f0
    if isPrime(f1):
        return f1
    return -1
