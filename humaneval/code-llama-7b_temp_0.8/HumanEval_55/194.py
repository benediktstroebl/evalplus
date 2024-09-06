

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    fib_nums = [1, 1]
    for i in range(2, n):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    return fib_nums[n - 1]

