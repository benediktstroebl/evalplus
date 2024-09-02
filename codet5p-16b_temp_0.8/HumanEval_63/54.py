

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

    fib = [0, 1, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        i = 3
        while i <= n:
            fib.append(fib[i-3] + fib[i-2] + fib[i-1])
            i += 1
    return fib[-1]

