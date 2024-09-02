

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
    if n <= 3:
        return 0 if n <= 1 else 2
    else:
        f_minus1, f_minus2, f_minus3, f_minus4 = 0, 0, 2, 0
        for _ in range(4, n + 1):
            f_n = f_minus1 + f_minus2 + f_minus3 + f_minus4
            f_minus4 = f_minus3
            f_minus3 = f_minus2
            f_minus2 = f_minus1
            f_minus1 = f_n
        return f_n

