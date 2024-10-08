

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

    fib = lambda x: ((1 + 5**.5)**x - (1 - 5**.5)) / (2**x * 5**.5)
    fib_num = fib(n - 1)
    return int(fib_num)

