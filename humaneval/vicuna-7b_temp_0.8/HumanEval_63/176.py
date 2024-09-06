

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
    # Use memoization to efficiently compute the fibfib numbers.
    fibfib_table = {n: fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n in range(10)}

    # Recursive approach.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n in fibfib_table:
        return fibfib_table[n]
    else:
        # Compute fibfib(n-1) + fibfib(n-2) + fibfib(n-3) and store the result in fibfib_table.
        fibfib_table[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
        return fibfib_table[n]