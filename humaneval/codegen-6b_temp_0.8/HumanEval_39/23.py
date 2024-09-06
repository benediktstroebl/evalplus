

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
    assert n > 0, 'n is less than 0'

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return pow(prime_fib(n-2) + prime_fib(n-1), 2)

