

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
    a = 0
    b = 1
    while b < n:
        b = a + b
        a = b - a
        if b % 2 == 0:
            continue
        else:
            a = b - a
    return b
