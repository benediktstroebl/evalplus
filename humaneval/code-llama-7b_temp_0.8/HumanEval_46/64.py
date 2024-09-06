

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
    a = 0
    b = 2
    c = 0
    d = 0
    n = n - 1
    while n > 0:
        if n % 4 == 1:
            a, b = b, b + c
        elif n % 4 == 2:
            c, d = d, c + d
        elif n % 4 == 3:
            a, b = b, a + b
        else:
            a, b = b, a + d
        n = n // 4
    return a + c
