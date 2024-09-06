

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
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    # Use a dictionary to store the values of the Fib4 sequence for speed
    fib4_dict = {4: 0, 5: 2, 6: 0, 7: 8}
    # The pattern is that every 4 numbers will be the same, so we only need to store the 4th number for speed
    for i in range(8, n+1):
        # Note that the index will be 1 more than the actual nth number we want
        fib4_dict[i] = fib4_dict[i-1] + fib4_dict[i-2] + fib4_dict[i-3] + fib4_dict[i-4]
    return fib4_dict[n]
