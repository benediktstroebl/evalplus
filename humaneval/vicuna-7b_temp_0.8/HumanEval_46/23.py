

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
    # using a loop to compute the fib4 number sequence
    # initialize the left and right pointers to the start and end of the sequence, respectively
    l, r = 0, 4
    
    # loop until the right pointer is greater than or equal to the target value
    while r < n:
        # compute the middle element of the sequence by adding the left and right pointers and subtracting 1
        m = l + r - 1
        
        # update the left and right pointers to the next element of the sequence
        l, r = r + 1, m + 1
    
    # return the n-th element of the fib4 sequence
    return l