

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
    if n <= 1:
        return 2

    fib_n = 1
    fib_n_minus_1 = 1
    for _ in range(n - 1):
        fib_n_plus_1 = fib_n_minus_1 + fib_n
        fib_n_minus_1, fib_n = fib_n, fib_n_plus_1

    return fib_n_plus_1

