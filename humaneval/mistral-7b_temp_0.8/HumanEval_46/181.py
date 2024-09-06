

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
    # precompute the previous 4 numbers
    prev = [0, 0, 2, 0]
    # fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    # the solution is always 4 digits long, but we need to start earlier because the
    # fib4 sequence is not periodic and its digits do not repeat.
    i = 4
    while i < n:
        prev[0] = prev[1]
        prev[1] = prev[2]
        prev[2] = prev[3]
        prev[3] = prev[0] + prev[1] + prev[2] + prev[3]
        i += 1
    return prev[3]
