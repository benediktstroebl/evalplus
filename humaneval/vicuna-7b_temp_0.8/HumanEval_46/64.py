

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
    # initialize variables with nth Fib4 number
    a = 0
    b = 1
    c = 1
    d = 0

    # loop through fib4 sequence
    for i in range(n-4, -1, -1):
        # compute fib4 number by adding previous four numbers
        result = a + b + c + d

        # update variables for next fib4 number
        a = b
        b = c
        c = d
        d = result

    return d