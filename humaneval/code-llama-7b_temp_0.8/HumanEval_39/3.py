

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
    for _ in range(n):
        a, b = b, a + b
        if b % 2 == 0 or b % 5 == 0:
            continue
        if is_prime(b):
            return b
    raise ValueError('No such Fibonacci prime')

