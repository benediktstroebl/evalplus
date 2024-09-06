

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
        raise ValueError("argument n must be greater than or equal to 1")
    a = 1
    b = 2
    c = 0
    for i in range(1,n):
        c = a + b
        a = b
        b = c
    return c
