

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

    f1 = 1
    f2 = 1
    pn = 2
    while pn <= n:
        pn = f1 + f2
        if is_prime(pn):
            n -= 1
            f1, f2 = f2, pn
    return pn

