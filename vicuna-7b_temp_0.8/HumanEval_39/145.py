

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
    if n < 2:
        raise ValueError("n should be a positive integer greater than 1")

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    if n % 3 == 0:
        return False

    fib = 0, 1
    p = 5
    while p < n:
        if fib[1] == p:
            fib = (fib[0] + fib[1]) % p
        p += 1
    return fib[0] % p == 1