

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
    # Define the recurrence relation
    def fibfib_rec(n):
        if n == 0:
            return 0
        elif n == 1:
            return 0
        else:
            return fibfib_rec(n-1) + fibfib_rec(n-2) + fibfib_rec(n-3)

    # Call the function and print the result
    return fibfib_rec(n)
