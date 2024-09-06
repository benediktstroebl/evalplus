

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    fib_cache = [0, 1]
    for i in range(2, n):
        fib_cache.append(fib_cache[i - 1] + fib_cache[i - 2])
    return fib_cache[n - 1]

