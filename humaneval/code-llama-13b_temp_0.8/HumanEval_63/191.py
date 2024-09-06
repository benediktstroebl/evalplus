

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
    if n <= 2:
        return n - 1
    n -= 3
    n1, n2, n3 = 0, 0, 1
    while n >= 0:
        nth = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = nth
        n -= 1
    return nth

