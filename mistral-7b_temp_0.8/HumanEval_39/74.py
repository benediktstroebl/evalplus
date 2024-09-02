

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
    while len(str(a)) + len(str(b)) < n:
        c = a + b
        a = b
        b = c
        if c == 1:
            return 2
        if is_prime(c):
            return c

