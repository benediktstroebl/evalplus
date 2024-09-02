

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
    assert n > 0
    assert n <= 1000000

    m = 0
    f = 1
    while m < n:
        f = f + m
        m = m + 1
    pf = is_prime(f)
    while m < n:
        f = f + m
        m = m + 1
        pf = pf and is_prime(f)

    return f if pf else prime_fib(n)
