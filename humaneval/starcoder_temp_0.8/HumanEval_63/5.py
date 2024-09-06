

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
    
    #first three values
    fib0 = 0
    fib1 = 0
    fib2 = 1

    #calculates the nth value
    for i in range(0, n):
        fib0 = fib1
        fib1 = fib2
        fib2 = fib0 + fib1
    
    return fib2
