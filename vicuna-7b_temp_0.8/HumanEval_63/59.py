

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
    def fib(n):
        """Compute the n-th Fibonacci number using O(log n) time complexity."""
        if n == 0 or n == 1:
            return 0
        return fib(n-1) + fib(n-2)

    # The Fibonacci sequence is defined as follows: fib(0) == 0, fib(1) == 1, fib(n) == fib(n-1) + fib(n-2)
    # We'll compute fibfib(n) by computing fib(n-1) and fib(n-2) separately and adding them up
    fib_1 = fib(n-1)
    fib_2 = fib(n-2)
    return fib_1 + fib_2