

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
    # This solution uses a sliding window approach to compute the sum of the last 3 fibonacci numbers, and then adds them to get the nth number in the sequence
    if n <= 3:
        return n
    else:
        fib1, fib2, fib3 = fibonacci(1), fibonacci(2), fibonacci(3)
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)