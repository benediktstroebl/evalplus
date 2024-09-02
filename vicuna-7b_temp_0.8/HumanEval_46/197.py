

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
    # https://discuss.leetcode.com/topic/8053/fibonacci-series-fibonacci-series-fib4-fib4n/3
    def fib4_rec(n: int, a: int, b: int):
        if n <= 1:
            return a
        return fib4_rec(n-1, b, a + b)
    return fib4_rec(n-1, 0, 1)