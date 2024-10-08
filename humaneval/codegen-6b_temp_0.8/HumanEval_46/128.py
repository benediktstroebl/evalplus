

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
    # I honestly don't know how to do this recursively so I'm just gonna do this instead
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    a = 0
    b = 1
    c = 0
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    return c
