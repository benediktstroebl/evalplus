

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
    if n == 2:
        return 3
    a = 1
    b = 2
    for _ in range(n - 3):
        a, b = b, (a + b) % 1000000
        if is_prime(b):
            return b
    return b
