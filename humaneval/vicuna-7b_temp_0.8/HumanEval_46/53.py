

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
    def fib(a, b):
        if b > 0:
            return fib(a, b-1) + fib(a, b-2)
        return fib(a-1, 0) + fib(a-1, 1)
    return fib(0, n-1) + fib(1, n-2) + fib(2, n-3) + fib(3, n-4)