

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
        return 2
    n1, n2 = 2, 3
    while True:
        if n2 > n:
            return n1
        n3 = n1 + n2
        if n3 > n:
            return n3
        n1, n2 = n2, n3
