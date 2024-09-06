

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
    assert 0 < n < 21, 'invalid input'
    p, f1, f2 = 2, 1, 1
    while n > 1:
        n -= 1
        p, f1, f2 = p * f1 + f2 * f1, f1, p
    return p

