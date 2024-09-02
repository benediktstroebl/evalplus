

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

    pf = lambda n: n if n <= 1 else pf(
        n - 1) + pf(n - 2) if [x for x in range(2, n) if n % x == 0] else n
    return pf(n)
