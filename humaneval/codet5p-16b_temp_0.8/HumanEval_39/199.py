

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

    a, b = 2, 3
    if n == 1:
        return a
    if n == 2:
        return b
    
    while n > 2:
        c = a + b
        if c % 2!= 0 and c % 3!= 0:
            a = b
            b = c
            n -= 1
    return c
