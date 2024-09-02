

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
    if n < 2:
        return 2
    if n < 3:
        return 1
    elif n % 2 == 0:
        return 1
    else:
        p = 1
        q = 1
        for i in range(2, n):
            p = p * (p - q) + q
            q = q * q + p
        while 1 in [p - 1, p, p + q]:
            p = p - 1
            q = q + 1
        return p
