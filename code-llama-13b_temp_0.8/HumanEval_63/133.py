

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
    cache = {}
    def helper(n):
        if n in cache:
            return cache[n]
        if n == 0:
            cache[0] = 0
            return 0
        if n == 1:
            cache[1] = 0
            return 0
        if n == 2:
            cache[2] = 1
            return 1
        result = helper(n-1) + helper(n-2) + helper(n-3)
        cache[n] = result
        return result
    return helper(n)


