

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

    curr = 0
    next = 1
    i = 0
    while i < n:
        curr, next = next, next + curr
        i += 1
        if not (curr % 2) and curr > 1 and is_prime(curr):
            n -= 1
    return curr

