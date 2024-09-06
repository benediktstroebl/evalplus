

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
    if n < 3:
        return 0
    current_term = 2
    prev1 = 0
    prev2 = 0
    prev3 = 0
    prev4 = 0
    for _ in range(3, n):
        current_term = prev4 + prev3 + prev2 + prev1
        prev4 = prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = current_term
    return current_term

