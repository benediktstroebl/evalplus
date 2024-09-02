

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
    # n = 1
    # for i in range(n):
    #     a, b = 1, 1
    #     for j in range(n):
    #         a, b = b, a + b
    #     return a
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
