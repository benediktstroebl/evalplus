

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
    last_1 = 0
    last_2 = 0
    last_3 = 0
    last_4 = 0
    for i in range(n):
        if i == 0:
            continue
        elif i == 1:
            last_1 = 0
            last_2 = 0
            last_3 = 0
            last_4 = 0
        elif i == 2:
            last_1 = 0
            last_2 = 2
            last_3 = 0
            last_4 = 0
        elif i == 3:
            last_1 = 0
            last_2 = 0
            last_3 = 0
            last_4 = 2
        elif i == 4:
            last_1 = 2
            last_2 = 0
            last_3 = 0
            last_4 = 0
        else:
            last_1 = last_4
            last_2 = last_3
            last_3 = last_2 + last_4
            last_4 = last_2 +
