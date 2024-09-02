

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    
    prev_one, prev_two, prev_three = 0, 0, 1

    for i in range(3, n):
        next_num = prev_one + prev_two + prev_three
        prev_one, prev_two, prev_three = prev_two, prev_three, next_num

    return prev_three
