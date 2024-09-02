

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 1:
        raise ValueError('n must be a positive integer')

    if n == 1 or n == 2:
        return n - 1

    # Use memoization to speed up the Fibonacci sequence
    memo = {}
    memo[1] = 1
    memo[2] = 2
    memo[3] = 3
    memo[4] = 5

    def fib_helper(n) -> int:
        if n in memo:
            return memo[n]
        else:
            memo_n = fib_helper(n - 1) + fib_helper(n - 2)
            memo[n] = memo_n
            return memo_n

    return fib_helper(n)

