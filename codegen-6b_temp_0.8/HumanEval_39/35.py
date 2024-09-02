

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
    assert n > 0, "n > 0 is required"
    if n == 1 or n == 2:
        return n
    else:
        a1, a2, a3 = 1, 2, 3
        for i in range(3, n):
            a3, a1, a2 = a1 + a2, a2, a3
        return a3
