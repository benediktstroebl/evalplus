

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    fib_number = [0, 1]
    if n < 2:
        return fib_number[n]
    else:
        for i in range(2, n + 1):
            fib_number.append(fib_number[i - 1] + fib_number[i - 2])
    return fib_number[n]
