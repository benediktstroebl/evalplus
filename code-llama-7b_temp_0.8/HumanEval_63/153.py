

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
    if n < 3:
        return 0
    # DP
    last, pre_last, pre_pre_last = 0, 0, 0
    for _ in range(3, n + 1):
        last, pre_last, pre_pre_last = pre_last, last, pre_last + pre_pre_last
    return last + pre_last + pre_pre_last

