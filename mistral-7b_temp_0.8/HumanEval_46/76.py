

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
    res = [0] * 4
    if n < 0:
        return None
    res[0], res[1] = 0, 0
    res[2], res[3] = 2, 0

    for i in range(4, n):
        res[i % 4] = res[(i - 1) % 4] + res[(i - 2) % 4] + res[(i - 3) % 4] + res[(i - 4) % 4]
    return res[n % 4]

