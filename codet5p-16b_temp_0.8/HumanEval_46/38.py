

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

    if n == 0 or n == 1:
        return 0
    fib4n_1 = 0
    fib4n_2 = 2
    fib4n = 0
    for i in range(2, n):
        fib4n = fib4n_1 + fib4n_2 + fib4n_1
        fib4n_1 = fib4n_2
        fib4n_2 = fib4n
    return fib4n
