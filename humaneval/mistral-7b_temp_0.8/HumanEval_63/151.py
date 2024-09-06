

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

    fibfib0 = 0
    fibfib1 = 0
    fibfib2 = 1

    if n == 0:
        return fibfib0
    if n == 1:
        return fibfib1
    if n == 2:
        return fibfib2

    for i in range(3, n + 1):
        fibfib3 = fibfib1 + fibfib2 + fibfib0
        fibfib0 = fibfib1
        fibfib1 = fibfib2
        fibfib2 = fibfib3

    return fibfib3
