

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    # 3 for loops is too slow

    # Memoization of the fibonacci sequence
    memo = {0: 0, 1: 0, 2: 1}

    def fib(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib(n - 1) + fib(n - 2) + fib(n - 3)
            return memo[n]

    def fibfib(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
            return memo[n]

    return fibfib(n)

