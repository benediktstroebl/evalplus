

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
    if n < 1:
        return 0
    if n == 1:
        return 2
    n_prime_fib = 0
    a = 1
    b = 2
    while a <= b:
        if is_prime(b):
            n_prime_fib = b
        if is_fibonacci(n):
            return n_prime_fib
        b = a + b
        a = b - a
    return n_prime_fib

