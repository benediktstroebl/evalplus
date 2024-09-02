

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
    assert n > 0, 'Fibonacci numbers do not exist for negative numbers'
    assert n > 3, 'Fibonacci numbers do not exist for less than 4 numbers'

    if n == 1:
        return 2
    if n == 2:
        return 3
    else:
        return prime_fib(n - 1) + prime_fib(n - 2)
