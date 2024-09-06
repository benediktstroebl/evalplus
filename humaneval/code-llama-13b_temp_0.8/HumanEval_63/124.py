

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
        return n - 1
    n -= 3
    cur = 0
    prev1 = 0
    prev2 = 1
    while n > 0:
        # Do the Fibonacci calculation,
        # and at the same time update the "previous" vars.
        cur, prev2, prev1 = cur + prev2 + prev1, cur, prev2
        n -= 1
    return cur













