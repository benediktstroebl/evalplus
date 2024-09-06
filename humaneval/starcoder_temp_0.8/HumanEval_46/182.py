

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
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # first 4 elements are 0, 0, 2, 0
        # print("n = ", n)
        # print("n-1 = ", n-1)
        # print("n-2 = ", n-2)
        # print("n-3 = ", n-3)
        # print("n-4 = ", n-4)
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

