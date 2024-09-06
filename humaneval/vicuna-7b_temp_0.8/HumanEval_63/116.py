

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
    n = max(n, 0)
    fib_list = []
    # use fibonacci recursion to find n-1 and n-2
    fib_list.append(1)
    fib_list.append(1)
    for i in range(n-1):
        fib_list.append(fib_list[i] + fib_list[i+1])
    fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list[-1]
