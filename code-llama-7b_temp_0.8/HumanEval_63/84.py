

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
    result = 0
    t1 = 0
    t2 = 0
    t3 = 0
    i = 0
    while i < n:
        if i < 2:
            result = i
        else:
            result = t1 + t2 + t3
            t3 = t2
            t2 = t1
            t1 = result
        i += 1

    return result

