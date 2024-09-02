

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
    
    # we create a list of fibonacci numbers in advance
    fib_nums = [0, 1, 1]
    
    # we append fibonacci numbers until we reach the value n
    while len(fib_nums) < n + 1:
        fib_nums.append(fib_nums[-1] + fib_nums[-2] + fib_nums[-3])
    
    # return the value at the index n
    return fib_nums[n]
