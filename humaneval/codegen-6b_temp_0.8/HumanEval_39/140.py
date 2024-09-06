

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
    fib_cache = [1, 1]
    while len(fib_cache) <= n:
        fib_cache.append(fib_cache[-1] + fib_cache[-2])
    return fib_cache[n]

