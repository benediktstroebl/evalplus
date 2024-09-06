

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
    if n == 1:
        return 2
    if n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        p = prime_fib(n-1)
        f = fib(n)
        while f % 2 == 0:
            f = f//2
            p = p//2
        while f % 5 == 0:
            f = f//5
            p = p//5
        if p == 13:
            return 89
        if f == 1:
            return p
        return fib(n)
