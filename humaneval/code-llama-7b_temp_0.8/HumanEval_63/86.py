

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
    # fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    # So, fibfib(n) == fibfib(n-2) + 2*fibfib(n-3)
    # Since fibfib(n-3) = fibfib(n-4) + fibfib(n-5)
    # fibfib(n) == fibfib(n-4) + 2*fibfib(n-4) + 2*fibfib(n-5)
    #              = fibfib(n-4) + 2*fibfib(n-4) + 2*fibfib(n-4) + 2*fibfib(n-5)
    #              = ...
    # fibfib(n) == (fibfib(n-4) + 3*fibfib(n-4))
    #              = (fibfib(n-4) + 3*fibfib(n-4)) + fibfib(n-5)
    #              = ...
    # fibfib(n) == fibfib(n-4) + 3*fibfib(n-4) + 2*fibfib(n-5) + 2*fibfib(n-5) + ... + fibfib(n-5)
    #              = fibfib(n-4) + 4*fibfib(n-4) + 3*fibfib(n-5)
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    elif n == 4:
        return 2

    a = 0
    b = 1
    c = 1
    d = 2
    e = 3

    for i in range(4, n):
        temp = d
        d = d + 3 * c + 2 * e
