

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
    # fibfib(3) == 1
    # fibfib(4) == 2
    # fibfib(5) == 3
    # fibfib(6) == 5
    # fibfib(7) == 8
    # fibfib(8) == 13
    # fibfib(9) == 21
    # ...
    if n <= 1:
        return n
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
