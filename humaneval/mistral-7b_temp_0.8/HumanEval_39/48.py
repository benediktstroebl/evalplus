

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
    p, p2, p3 = 2, 3, 5
    i = 0
    while True:
        i += 1
        a, b = b, a + b
        p2 = p * p2
        p3 = p3 * p3 * p3
        if a < p:
            continue
        if a % p == 0:
            continue
        if a % p2 == 0:
            continue
        if a % p3 == 0:
            continue
        return a

