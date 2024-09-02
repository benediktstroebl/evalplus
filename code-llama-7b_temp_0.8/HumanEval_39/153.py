

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
    a, b = 1, 2
    for _ in range(n):
        a, b = b, a + b
        p = 5
        while p * p <= b:
            if b % p == 0:
                break
            p += 2
        if p * p > b:
            return b
