

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
    assert isinstance(n, int) and n >= 0, "n must be a non-negative int"
    if n < 3:
        return n
    elif n == 3:
        return 2
    fib, fib_prev, fib_prev_prev = 0, 1, 2
    for _ in range(3, n + 1):
        fib, fib_prev, fib_prev_prev = fib_prev + fib_prev_prev + fib, fib, fib_prev
    return fib
