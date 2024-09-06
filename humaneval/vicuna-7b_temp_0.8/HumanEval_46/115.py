

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
    results = []
    # check for edge cases
    if n <= 0:
        return 0
    elif n == 1:
        return 2
    # insertion sort the sequence
    results.append(2)
    results.append(0)
    for i in range(1, n):
        j = (i-1) % 4 + 1
        results[i] = results[j] + results[i-j]
    return results[n-1]
