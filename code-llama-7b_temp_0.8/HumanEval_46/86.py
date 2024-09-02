

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
    # The code below is a recursive version.  It may work for small numbers, but
    # for larger numbers, it will raise a stack overflow error.
    # return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

    # The code below is an iterative version.  It takes a while to run, but it
    # won't raise a stack overflow error.
    # It works by maintaining four variables that track the Fib4 sequence up to
    # a certain point.  It's important to understand that the Fib4 sequence
    # is a sequence of partial sums of the Fibonacci sequence.  A good exercise
    # is to write a function to compute the n-th element of the Fibonacci sequence
    # without recursion.

    # Note that the first argument to the Fib4 function below is the number of
    # elements of the Fibonacci sequence that we've already computed.  We
    # initialize the variables to 1 because we've already computed the first
    # two elements.
    if n < 0:
        return None
    fib4_0 = 0
    fib4_1 = 0
    fib4_2 = 2
    fib4_3 = 0
    for i in range(1, n):
        fib4_0, fib4_1, fib4_2, fib4_3 = fib4_1, fib4_2, fib4_2 + fib4_3, fib4_3
    return fib4_2

