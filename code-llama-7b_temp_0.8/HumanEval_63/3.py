

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
    fibfib_cache = {}

    def _fibfib(n: int) -> int:
        if n < 3:
            return 0
        if n in fibfib_cache:
            return fibfib_cache[n]
        fibfib_cache[n] = _fibfib(n - 1) + _fibfib(n - 2) + _fibfib(n - 3)
        return fibfib_cache[n]

    return _fibfib(n)

