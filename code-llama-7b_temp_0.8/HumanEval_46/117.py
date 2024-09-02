

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
    if n < 0:
        raise ValueError('fib4 number can not be negative')
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    prev_prev_prev_prev = 0
    prev_prev_prev = 2
    prev_prev = 0
    prev = 0
    current = 2
    for _ in range(n - 4):
        prev_prev_prev_prev = prev_prev_prev
        prev_prev_prev = prev_prev
        prev_prev = prev
        prev = current
        current = prev_prev_prev + prev_prev + prev + prev_prev_prev_prev
    return current

