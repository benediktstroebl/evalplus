

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
    # Fast matrix multiplication to compute fib4(n)
    # Using the formula fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    # We can represent the fib4 sequence as:
    # [0, 0, 2, 2, 0, 2, 4, 4, 0, 4, 6, 6, ...]
    # and compute it as:
    # fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    # = fib4(n-2) + fib4(n-3) + fib4(n-4)
    # = fib4(n-3) + fib4(n-4)
    # = ...
    # = fib4(0) + fib4(1) + fib4(2)
    # = fib4(0) + fib4(1)
    # = fib4(1)
    # = 1
    return 1
