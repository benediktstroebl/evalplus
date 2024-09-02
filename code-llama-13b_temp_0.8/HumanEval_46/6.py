

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

    # runnning time complexity O(n)
    # space complexity O(1)
    # check input 
    if not isinstance(n, int) or n < 0:
        raise TypeError('n must be a positive int')
    # if n is 0 or 1 
    if n == 0 or n == 1:
        return 0
    # initialize variables for n - 1 and n - 2 
    f_n_minus_1 = 0
    f_n_minus_2 = 0
    f_n_minus_3 = 0
    f_n_minus_4 = 0
    # iterate 
    for i in range(n - 1):
        # compute the n-1 and n-2
        f_n_minus_1 = f_n_minus_2
        f_n_minus_2 = f_n_minus_3 + f_n_minus_4
        # compute the new n-3 and n-4
        f_n_minus_3 = f_n_minus_1 + 2 * f_n_minus_2
        f_n_minus_4 = f_n_minus_2 + f_n_minus_3
    # return the last number 
    return f_n_minus_2 + f_n_minus_3 + f_n_minus_4


