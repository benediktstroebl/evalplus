

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

    # Fib4(0) = 0, Fib4(1) = 0, Fib4(2) = 2, Fib4(3) = 0, Fib4(4) = 0, Fib4(5) = 4, Fib4(6) = 8, Fib4(7) = 14, Fib4(8) = 32, ...
    a, b, c, d, e = 0, 0, 2, 0, 0
    if n < 2:
        return a
    elif n < 3:
        return b
    elif n < 4:
        return c
    elif n < 5:
        return d
    elif n < 6:
        return e
    for i in range(5, n):
        if i < 6:
            a, b, c, d, e = e, a + b + c + d, e, a, b
        else:
            a, b, c, d, e = e, a + b + c + d, e,
