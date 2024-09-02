

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
        raise ValueError("n should be a positive number.")
    if n % 2 == 0:
        a, b = 2, 1
    else:
        a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    if is_prime(b):
        return b
    else:
        return -1
