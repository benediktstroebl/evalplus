

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

    fib_dict = {0: 0, 1: 1, 2: 2, 3: 0}
    def helper(n: int):
        if n in fib_dict:
            return fib_dict[n]
        else:
            fib_dict[n] = helper(n - 1) + helper(n - 2) + helper(n - 3) + helper(n - 4)
        return fib_dict[n]
    return helper(n)

