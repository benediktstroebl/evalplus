

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

    # initialize variables to return value
    a = 0
    b = 1
    c = 2
    d = 1

    # loop through values until n is reached
    while n > 0:
        # calculate sum of fib4 values
        sum = a + b + c + d
        # return sum
        return sum

    # return default value if n is less than 0
    return 0
