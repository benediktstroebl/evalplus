

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
    a1, a2 = 1, 1
    for i in range(n - 2):
        a1, a2 = a2, a1 + a2
    if (n - 1) % 2 == 0:
        return a2
    return a1 + a2

