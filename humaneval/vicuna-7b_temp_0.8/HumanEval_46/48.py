

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
    # Since the fib4 sequence is defined by a simple addition of the previous 4 terms, we can store the values of the previous 4 terms in a list and add them up in a single addition
    values = [0, 0, 0, 0]
    result = values[0]
    for i in range(1, n+1):
        result = values[i]
    return result