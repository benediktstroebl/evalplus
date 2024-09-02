

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
    # The FibFib sequence is 0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # So, we can just compute the sum of the previous two numbers to get the next one
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
