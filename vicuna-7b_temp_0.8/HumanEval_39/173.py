

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
        raise ValueError("n must be greater than 1")

    a, b = 0, 1
    limit = n
    while b < limit:
        if b == 2:
            if (a % b) == 0:
                return b
            a += 1
        b += a
    return b
