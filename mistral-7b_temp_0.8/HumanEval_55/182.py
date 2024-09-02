

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # Pre-calculate the 2 first fibonacci numbers
    a = 0
    b = 1

    # While we are not at the n-th fibonacci number
    # We increment the next fibonacci number and check if it is equal to n
    while a < n:
        c = a + b

        # If it is equal to n we return it
        if c == n:
            return c

        a = b
        b = c

    return n

