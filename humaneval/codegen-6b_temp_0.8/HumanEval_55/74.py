

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    fib_numbers = [1]

    while not len(fib_numbers) == n:
        n = len(fib_numbers)
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    return fib_numbers[-1]

