

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    "*** YOUR CODE HERE ***"
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

