

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
    assert isinstance(n, int)
    assert n >= 0
    if n <= 2:
        return n
    prev_prev_fib = 0
    prev_fib = 0
    cur_fib = 1
    for _ in range(n - 2):
        prev_prev_fib = prev_fib
        prev_fib = cur_fib
        cur_fib = prev_fib + prev_prev_fib
    return cur_fib

