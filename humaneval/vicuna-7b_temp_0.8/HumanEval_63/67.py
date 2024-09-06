

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
    def fib(x):
        """A helper function that returns the n-th Fibonacci number."""
        if x <= 1:
            return 0
        elif x == 2:
            return 1
        else:
            return fib(x-1) + fib(x-2)

    def fibfib(n):
        """The main function that computes the n-th Fibfib number."""
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    return fibfib(n)