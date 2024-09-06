

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
    # Fib4 number sequence
    # n = 4, a(n) = 0
    # n = 3, b(n) = 0
    # n = 2, a(n) = 2, b(n) = 0
    # n = 1, a(n) = 0, b(n) = 0
    # n = 0, a(n) = 0, b(n) = 0
    a, b = 0, 0
    for i in range(n):
        a, b = (a + b) % 16, (a - b) % 16
    return a
