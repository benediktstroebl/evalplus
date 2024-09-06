

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
    # fib4(0) = 0
    # fib4(1) = 0
    # fib4(2) = 2
    # fib4(3) = 0
    # fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    # ...
    # fib4(7) = 0 + 0 + 1 + 4 = 5
    # fib4(8) = 5 + 0 + 2 + 4 = 9
    # fib4(9) = 9 + 0 + 2 + 4 = 15
    # ...
    # fib4(19) = 15 + 14 + 13 + 12 + 11 + 10 = 981
    # fib4(20) = 981 + 980 + 982 + 983 + 984 + 985 = 10497
    # ...

    # fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    result = 0
    for i in range(n-4, -1, -1):
        result = fib4(i) + result
    return result