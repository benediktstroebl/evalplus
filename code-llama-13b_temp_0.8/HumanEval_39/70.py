

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
    # by default fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3
    if n in [1, 2]:
        return 1
    fib = 1
    fib2 = 1
    n -= 2  # 0-based index
    while n >= 0:
        fib, fib2 = fib2, fib + fib2
        if is_prime(fib2):
            n -= 1
    return fib2

