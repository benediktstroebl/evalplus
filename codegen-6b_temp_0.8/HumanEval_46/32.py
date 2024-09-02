

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
    def recur(n, k):
        if n < 0:
            return 0
        elif n == 0:
            return k
        else:
            return recur(n-1, k) + recur(n-2, k) + recur(n - 3, k) + recur(n - 4, k)
    if n < 0:
        return 0
    elif n == 0:
        return 0
    else:
        return recur(n - 1, 1) + recur(n - 2, 2) + recur(n - 3, 3) + recur(n - 4, 4)


