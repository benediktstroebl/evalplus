

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
    for i in range(n):
        c = a + b
        if c > n:
            break
        for p in range(2, c):
            if c % p == 0:
                break
        else:
            a, b = b, c
            return c

