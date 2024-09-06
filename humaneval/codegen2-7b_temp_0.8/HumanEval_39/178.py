

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
    p = [1, 2]
    q = 3
    n = n - 1
    while n > 1:
        q = p[0] + p[1]
        p[0] = p[1]
        p[1] = q
        n = n - 1
    return q
