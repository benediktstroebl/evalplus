

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    a = 0
    b = 1
    fibs = [1, 1] # adding 1 to index 0 and 1 to index 1

    if n < 2:
        return fibs[n]
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            fibs.append(c)
    return fibs[n]
