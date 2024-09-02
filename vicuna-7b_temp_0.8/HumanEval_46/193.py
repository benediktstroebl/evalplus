

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
    # Initialize variables with starting values
    a = 0
    b = 1

    # Calculate intermediate values
    c, d, e, f = 2, 1, 0, 0

    # Combine intermediate values to compute the final result
    result = c
    for i in range(n-4, -1, -1):
        result = a + b + c + d
        a, b, c, d = d, c, b, result

    return result