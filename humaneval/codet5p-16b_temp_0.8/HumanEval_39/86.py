

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

    p1 = 2
    p2 = 3
    i = 4
    while i < n:
        p1, p2 = p2, p1 + p2
        if is_prime(p2):
            i += 1
    return p2

