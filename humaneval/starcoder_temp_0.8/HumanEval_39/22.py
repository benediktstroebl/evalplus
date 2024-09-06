

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

    i = 2
    f1 = 1
    f2 = 2

    while i < n:
        fn = f1 + f2
        f1 = f2
        f2 = fn
        if is_prime(fn):
            i += 1

    return fn
