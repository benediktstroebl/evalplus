

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
        raise ValueError('n must be greater than 0')
    if n == 1:
        return 2
    a, b = 1, 2
    n -= 1
    while n:
        a, b = b, (a + b)
        if a < b:
            b = a + b
            continue
        if is_prime(b):
            n -= 1
        if n == 0:
            break
    return b

