from collections import Sequence
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    The n-th element of the FibFib sequence is retrieved."""
    fibfib_seq = Sequence(fibfib_gen(n))
    return next(fibfib_seq)