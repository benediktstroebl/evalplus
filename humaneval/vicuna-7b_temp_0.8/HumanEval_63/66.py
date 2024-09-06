

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
    # Check if the input is 0
    if n == 0:
        return 0
    
    # Calculate the first two terms
    a = 0
    b = 1
    
    # Calculate the rest of the terms by using the above two terms
    for i in range(3, n):
        a, b = b, a + b
    
    return a