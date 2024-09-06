

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
    # The 3 previous fib numbers are required to calculate the n-th fib number
    a = fib(n-3)
    b = fib(n-2)
    c = fib(n-1)
    # The formula: c = a + b + fib(n-3)
    d = a + b + fibfib(n-3)
    # The formula: d = c + fib(n-2)
    e = c + fibfib(n-2)
    # The formula: e = d + fib(n-1)
    f = d + fibfib(n-1)
    return f
