

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

    fib = []
    fib.append(1)
    fib.append(2)
    i = 2
    while i < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n - 1]

