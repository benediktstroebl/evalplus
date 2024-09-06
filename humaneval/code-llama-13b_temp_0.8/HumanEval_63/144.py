

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
    if n <= 3:
        return n - 2
    fibfib_last = 2
    fibfib_last_last = 1
    fibfib_last_last_last = 0

    for i in range(3, n):
        tmp = fibfib_last + fibfib_last_last + fibfib_last_last_last
        fibfib_last_last_last = fibfib_last_last
        fibfib_last_last = fibfib_last
        fibfib_last = tmp
    return fibfib_last
