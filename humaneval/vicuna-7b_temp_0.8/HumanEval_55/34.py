

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # perform recursion and memoization
    if n < 2:
        return n, 1
    if n < 1000:
        # use closed-form solution for small numbers
        return (fib(n-1) + fib(n-2), fib(n-1) + fib(n-2))
    else:
        # use memoization for larger numbers
        if n in memo:
            return memo[n], memo[n-1]
        else:
            memo[n] = fib(n-1) + fib(n-2)
            memo[n-1] = memo[n]
            return memo[n], memo[n-1]
