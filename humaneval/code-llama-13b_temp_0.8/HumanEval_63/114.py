

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

    # 0th and 1st element of fibfib are 0
    if n == 1 or n == 2:
        return 0

    # 2nd and 3rd element of fibfib are 1
    if n == 3 or n == 4:
        return 1

    # if n is a positive integer above 4, calculate it with the recurrence relation
    result = fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    return result

