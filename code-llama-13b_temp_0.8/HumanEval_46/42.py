

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

    if n < 0:
        raise ValueError("n must be a positive number")

    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    # Initialization
    i = 4
    fib1 = 0
    fib2 = 0
    fib3 = 2
    fib4 = 0

    # Implementation
    while i < n:
        fib4 = fib3 + fib2 + fib1 + fib4
        fib1 = fib2
        fib2 = fib3
        fib3 = fib4
        i += 1

    return fib4

