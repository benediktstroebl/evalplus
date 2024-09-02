

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
    if n == 2:
        return 1
    elif n < 2:
        return 0

    # Using a 2D array to store the n-th and (n-1)-th element
    # of the fibfib sequence
    array = [[0, 0]]
    for _ in range(n - 1):
        array.append([array[-1][1], array[-1][0] + array[-1][1] + array[-1][2]])
        array[-1].append(array[-2][1])

    return array[-1][1]
