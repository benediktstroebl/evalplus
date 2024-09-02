

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
    from math import sqrt

    if n < 1:
        raise ValueError("n cannot be less than 1")

    if n == 1:
        return 2

    if n == 2:
        return 3

    a, b = 2, 3
    fib = 3

    while fib < n:
        a, b = b, a + b
        fib = a + b
        if is_prime(fib):

            if n % 2 == 0 and fib != n:
                pass
            else:
                return fib

    raise ValueError(f"{n} is not a Fibonacci number")

