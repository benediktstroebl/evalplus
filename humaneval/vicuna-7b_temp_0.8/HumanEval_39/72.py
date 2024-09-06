

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
    f = 0
    n1 = 1
    n2 = 1
    i = 2
    while i <= n:
        f += (i % 2) * (n1 ** i)
        n1 += n2
        n2 = n1 - n2
        i += 1
    return f % 2 ** n - 1
