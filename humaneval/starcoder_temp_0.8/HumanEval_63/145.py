

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
    if n <= 1:
        return 0
    if n == 2:
        return 1
    previous_previous = 0
    previous = 0
    current = 1
    i = 2
    while i < n:
        previous, previous_previous, current = current, previous, previous + previous_previous
        i += 1
    return current
