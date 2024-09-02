

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    start = time()
    if n < 0:
        raise ValueError("n must be non-negative")

    # 1. start with the default base case.
    # 2. fib(1) = 1
    # 3. fib(0) = 0
    # 4. fib(n) = fib(n-1) + fib(n-2)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

    # NOTE: in the textbook, get the last 2 results
    # and return the sum
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     return fib(n - 1) + fib(n - 2)

    print(f"fib({n}) took {time() - start:.5f}s")
