

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
        raise ValueError('Input n must be >= 0')

    fib_array = [0, 0, 1]
    for i in range(3, n+1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2] + fib_array[i - 3])

    return fib_array[n]

