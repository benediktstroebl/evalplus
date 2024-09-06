

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
    # Check if the input n is in range
    if n < 0 or n > 20:
        raise ValueError("Input n must be in range 0 to 20")
    
    # Compute and store the n-th FibFib number
    n_fibfib = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    
    return n_fibfib
