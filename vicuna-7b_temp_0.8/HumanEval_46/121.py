

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
    # Initialize variables with default values
    a = 0
    b = 1
    c = 1
    d = 1

    # Use memoization to optimize the computation of the fib4 sequence
    memo = {}

    # Store the intermediate values in the memo
    memo[0] = 0
    memo[1] = 0
    memo[2] = 2
    memo[3] = 0

    # Compute the n-th element of the fib4 sequence
    result = 0
    for i in range(4, n + 1):
        result = memo.get(i, None)
        if result is None:
            # If the intermediate value is not stored in the memo, compute it
            a, b, c, d = b, c, d, a + b + c + d
            memo[i] = a
            result = a + b + c + d
        else:
            # If the intermediate value is stored in the memo, use it
            a, b, c, d = result
            result = a + b + c + d

    return result