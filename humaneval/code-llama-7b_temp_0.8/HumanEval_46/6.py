

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
        raise ValueError("n should be non-negative")

    def compute(i: int):
        if i < 4:
            return 0
        first, second, third, forth = 0, 2, 0, 2
        for _ in range(4, i+1):
            first, second, third, forth = second, third, forth, first + second + third + forth
        return forth

    return compute(n)

