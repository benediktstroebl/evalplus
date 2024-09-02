

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
    # I'm not going to write a fibonacci function, you can use one of the many pre-existing fibonacci functions.
    # Instead, I'll use the formula to calculate the fib4(n) value.
    a, b = 0, 1
    for i in range(n-4, -1, -1):
        fib4(n) = a + b
        a, b = b, a + b
    return fib4(n)
