

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
    nums = [0] * (n + 1)
    nums[0], nums[1] = 0, 0
    nums[2], nums[3] = 2, 0
    for i in range(4, n + 1):
        nums[i] = nums[i-1] + nums[i-2] + nums[i-3] + nums[i-4]
    return nums[n]

