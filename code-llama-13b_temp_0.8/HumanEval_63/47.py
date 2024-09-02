

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
    assert n >= 1
    if n <= 3:
        return n - 1
    prev2 = 0
    prev1 = 1
    res = 1
    for i in range(3, n):
        res = prev2 + prev1 + prev1
        prev2 = prev1
        prev1 = res
    return res
