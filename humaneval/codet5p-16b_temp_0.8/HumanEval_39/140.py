

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

    a, b = 0, 1
    while n > 0:
        c = a + b
        if c == 0:
            continue
        if not c > 1:
            continue
        if not is_prime(c):
            continue
        a, b = b, c
        n -= 1
    return b
