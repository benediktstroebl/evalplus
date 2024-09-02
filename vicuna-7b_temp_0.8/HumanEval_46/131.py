

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
    # The fib4 sequence is the sum of the previous 4 numbers
    # So, we start with the 0th and 1st number and compute the sum of their sum
    # Then, we add the 2nd and 3rd number, and so on, until we have the sum of the previous n-1 numbers
    # and add the nth number to get the final result.
    return 4 + (2 + (3 + 0))