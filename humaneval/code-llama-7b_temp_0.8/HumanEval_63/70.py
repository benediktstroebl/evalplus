

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
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    last_n = 0
    pen_last_n = 0
    third_last_n = 1

    for i in range(3, n + 1):
        temp = last_n + pen_last_n + third_last_n
        last_n = pen_last_n
        pen_last_n = third_last_n
        third_last_n = temp

    return temp

