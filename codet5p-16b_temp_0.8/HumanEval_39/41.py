

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

    a = 1
    b = 2
    c = 3
    for _ in range(n-1):
        a = b
        b = c
        c = a + b
        if not is_prime(c):
            c = b + a
            if is_prime(c):
                return c
    return c

