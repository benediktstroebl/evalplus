

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
    # Using a dictionary to store the calculated values
    # The dictionary keys are the indices of the fib4 sequence and the values are the corresponding values
    fib4_dict = {i: 0 for i in range(4, n+1)}
    result = 0
    for i in range(1, n-1):
        result = fib4_dict[i] + fib4_dict[i-1] + fib4_dict[i-2] + fib4_dict[i-3]
        fib4_dict[i] = result
    return fib4_dict[n-1]
