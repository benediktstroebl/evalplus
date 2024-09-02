

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
    if n < 2:
        return n

    # Create an array that will hold the fibfib sequence
    sequence = [0, 0, 1]

    # Calculate the fibfib sequence
    for _ in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])

    return sequence[n]

