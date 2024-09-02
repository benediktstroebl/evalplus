

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
    assert isinstance(n, int), 'n is not an integer'
    assert n >= 1, 'n is less than 1'

    if n <= 1:
        return n

    if n <= 3:
        return 2

    fib_n = fib(n-1) + fib(n-2)

    while not is_prime(fib_n):
        fib_n = fib(n-1) + fib(n-2)

    return fib_n

