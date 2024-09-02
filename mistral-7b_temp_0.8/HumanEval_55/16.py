

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    fib_dict = {1: 1, 2: 1}

    if n in fib_dict:
        return fib_dict[n]

    fib_dict[n] = fib(n - 1) + fib(n - 2)
    return fib_dict[n]
