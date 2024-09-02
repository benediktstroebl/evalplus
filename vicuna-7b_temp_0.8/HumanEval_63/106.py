

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
    # Find the two numbers in the Fibonacci sequence that lead up to n
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    # Compute the sum of a, b, and the previous two values
    c = a + b
    # Return the computed value
    return c
