

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
    f = [0, 1, 1, 2, 3, 5]
    if n < 0:
        return None
    if n < 6:
        return f[n]
    for i in range(6, n+1):
        f.append(f[i - 1] + f[i - 2] + f[i - 3] + f[i - 4])
    return f[n]

