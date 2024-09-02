

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
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    elif n == 4:
        return 3
    else:
        x = [0 for i in range(n)]
        x[0] = 0
        x[1] = 0
        x[2] = 2
        x[3] = 0
        x[4] = 3
        for i in range(5, n):
            x[i] = x[i - 1] + x[i - 2] + x[i - 3] + x[i - 4]
        return x[n - 1]

