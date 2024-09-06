

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
    def _fib4(n, a, b, c, d):
        if n < 1:
            return 0
        if n == 1:
            return a
        if n == 2:
            return b
        if n == 3:
            return c
        if n == 4:
            return d

        return _fib4(n - 1, a, b, c, d) + _fib4(n - 2, a, b, c, d) + _fib4(n - 3, a, b, c, d) + _fib4(n - 4, a, b, c, d)

    if n < 1:
        return 0

    return _fib4(n, 0, 2, 0, 0)

