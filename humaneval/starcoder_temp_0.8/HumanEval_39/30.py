

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
    i = 2
    f1 = 0
    f2 = 1
    while i < n:
        f = f1 + f2
        f1 = f2
        f2 = f
        if is_prime(f):
            i = i + 1
    return f
