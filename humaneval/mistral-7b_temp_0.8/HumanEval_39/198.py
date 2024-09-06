

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
    n = int(n)
    if n < 1:
        raise ValueError('n should be at least 1')
    a, b = 1, 1
    while a <= n:
        if is_prime(a) and a == fibonacci(a):
            return a
        a, b = b, a + b
    return n

