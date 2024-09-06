

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
    fib4_n = {}

    for i in range(0, n+1):
        if i <= 3:
            fib4_n[i] = 0
        elif i == 4:
            fib4_n[i] = 2
        else:
            fib4_n[i] = fib4_n[i-1] + fib4_n[i-2] + fib4_n[i-3] + fib4_n[i-4]

    return fib4_n[n]

