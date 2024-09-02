

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
        return None

    a = 2
    p = 3
    if n == 1:
        return a
    elif n == 2:
        return a + 1

    while p < n:
        a = a + p
        p = p + 2

    return a
