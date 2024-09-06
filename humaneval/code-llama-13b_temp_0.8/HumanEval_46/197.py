

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
    # The first two values of the sequence are 0 and 2
    if n in [0, 1]:
        return 0
    elif n in [2, 3]:
        return 2
    else:
        # For every other value in the sequence, we want to find the sum of the previous 4 values
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
