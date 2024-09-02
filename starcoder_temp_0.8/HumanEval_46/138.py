

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
    # initialize a list with the first four numbers of the sequence
    fib4_list = [0, 0, 2, 0]

    # check the value of n and return the last element of the list.
    if n <= 4:
        return fib4_list[n]

    # loop from 4 to n
    for i in range(4, n):
        # store the last four elements of the list in variables
        a = fib4_list[-1]
        b = fib4_list[-2]
        c = fib4_list[-3]
        d = fib4_list[-4]
        # update the last four elements of the list using the recurrence relation of the fibonacci sequence
        fib4_list[-1] = a + b + c + d
        fib4_list[-2] = a + b
        fib4_list[-3] = a
        fib4_list[-4] = 0

    return fib4_list[-1]
