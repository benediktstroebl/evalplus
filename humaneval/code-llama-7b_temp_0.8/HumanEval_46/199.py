

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
    if n < 2:
        return n

    # Create an array to store the results
    results = [0] * (n + 1)

    # Base case
    results[0] = 0
    results[1] = 0
    results[2] = 2
    results[3] = 0

    # General cases
    for i in range(4, n + 1):
        results[i] = results[i - 1] + results[i - 2] + results[i - 3] + results[i - 4]

    return results[n]

