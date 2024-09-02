

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

    a = 0
    b = 0
    c = 0
    fibfib_num = 0

    if n == 0:
        return fibfib_num
    if n == 1:
        return fibfib_num
    if n == 2:
        return 1
    if n == 3:
        return 1

    for i in range(3, n + 1):
        c = a + b + fibfib_num
        a = b
        b = c
        fibfib_num = a
    return fibfib_num

