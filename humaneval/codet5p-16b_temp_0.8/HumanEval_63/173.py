

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

    fib0 = 0
    fib1 = 1
    fib2 = 1

    if n < 3:
        return 0 if n < 2 else 1

    for _ in range(3, n+1):
        fib3 = fib0 + fib1 + fib2
        fib0 = fib1
        fib1 = fib2
        fib2 = fib3

    return fib3
