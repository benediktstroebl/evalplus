

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
    if not isinstance(n, int) or n < 1:
        raise ValueError("The input has to be an integer bigger than 0")

    # Initialize an empty list of length n
    cache = [None] * n

    # Compute the first 3 elements
    cache[0] = 0
    cache[1] = 0
    cache[2] = 1

    # Compute the rest of the elements
    for idx in range(3, n):
        cache[idx] = cache[idx - 1] + cache[idx - 2] + cache[idx - 3]

    # Return the n-th element
    return cache[n - 1]

