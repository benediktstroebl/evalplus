

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
    previous_fib4 = 0
    current_fib4 = 1
    next_fib4 = 0
    if n == 0 or n == 1:
        return previous_fib4
    elif n == 2:
        return current_fib4
    elif n == 3:
        return next_fib4
    elif n == 4:
        return 2

    for i in range(4, n):
        next_fib4 = previous_fib4 + current_fib4 + next_fib4 + fib4(i-1)
        previous_fib4 = current_fib4
        current_fib4 = next_fib4
    return next_fib4

