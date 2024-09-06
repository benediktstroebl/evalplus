

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    from typing import Tuple

    def compute_fib4(i: int) -> Tuple[int, int, int, int]:
        if i < 4:
            if i == 0:
                return (0, 0, 0, 0)
            elif i == 1:
                return (0, 0, 0, 2)
            elif i == 2:
                return (0, 0, 2, 0)
            else:
                return (0, 2, 0, 0)
        else:
            p1, p2, p3, p4 = compute_fib4(i-1)
            return (p1, p2, p3, p4 + p1 + p2 + p3)

    _, _, p3, _ = compute_fib4(n)
    return p3

