

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
    a, b, c = 1, 1, 0
    for i in range(n):
        a, b = b, a+b
        c = c + 1
    return c

