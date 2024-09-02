

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
    # fibfib(0) == 0
    # fibfib(1) == 0
    # fibfib(2) == 1
    if n <= 2:
        return n
    # The memoization cache
    cache = {0: 0, 1: 0, 2: 1}

    def fibfib_memoized(n: int) -> int:
        """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
        fibfib(0) == 0
        fibfib(1) == 0
        fibfib(2) == 1
        fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
        >>> fibfib_memoized(1)
        0
        >>> fibfib_memoized(5)
        4
        >>> fibfib_memoized(8)
        24
        """
        if n not in cache:
            cache[n] = fibfib_memoized(n - 1) + fibfib_memoized(n - 2) + fibfib_memoized(n - 3)
        return cache[n]
    return fibfib_memoized(n)
