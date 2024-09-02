

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # check for zero and negative arguments
    if n <= 0:
        raise ValueError("Invalid argument")

    # if n is 0 or 1, return 1
    if n == 0:
        return 1
    elif n == 1:
        return 1

    # if n is 2, return 1
    elif n == 2:
        return 1

    # calculate previous numbers
    a, b = 0, 1
    for _ in range(n-2):
        a, b = b, a + b

    # return n-th number
    return a