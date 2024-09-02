

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
    if n < 1:
        return 2
    n = n - 1

    while True:
        a = 1
        b = 1
        # step one
        c = a + b
        # step two
        if is_prime(c):
            return c
        else:
            a = b
            b = c
            c = a + b
            if is_prime(c):
                return c

        n = n - 1

