

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
        return n

    fibfib_1 = 0
    fibfib_2 = 0
    fibfib_3 = 1
    for _ in range(3, n + 1):
        fibfib_4 = fibfib_3 + fibfib_2 + fibfib_1
        fibfib_1 = fibfib_2
        fibfib_2 = fibfib_3
        fibfib_3 = fibfib_4
    return fibfib_3

