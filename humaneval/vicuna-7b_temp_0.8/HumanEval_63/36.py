

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
    # Create a list to store the fibfib numbers
    fibfib_numbers = [0, 0]
    for i in range(n-1, -1, -1):
        fibfib_numbers.append(fibfib_numbers[i-2] + fibfib_numbers[i-3])
    return fibfib_numbers[n-2]