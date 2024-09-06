

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
    else:
        return fib_dict[n - 1] + fib_dict[n - 2]

