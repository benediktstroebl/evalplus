

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
    # Validate the input
    if n < 2:
        return 0

    # Make 2 variables to hold the current and next FibFib numbers
    curr_fibfib = 0
    next_fibfib = 0

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Compute the next FibFib number
        next_fibfib = curr_fibfib + next_fibfib + curr_fibfib
        # Update the current number to be the next number
        curr_fibfib = next_fibfib

    # Return the answer
    return next_fibfib

