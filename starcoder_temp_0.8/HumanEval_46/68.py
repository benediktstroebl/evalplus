

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
    #A = 0, B = 0, C = 2, D = 0
    #1. Write down the recurrence relation
    #2. Identify base cases (n <= 3)
    #3. Identify the pattern of the general solution.
    A, B, C, D = 0, 0, 2, 0
    for i in range(n):
        A = B
        B = C
        C = D
        D = A + B + C
    return D
