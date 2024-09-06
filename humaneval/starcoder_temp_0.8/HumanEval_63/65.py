

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
    if n < 0:
        raise ValueError("n must be a positive integer")
    fib = [0] * (n+1)
    fib[1] = 0
    fib[2] = 1
    if n >= 2:
        for i in range(3, n+1):
            fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
