

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
    # A table for precomputing the values of fib4(n) for small values of n
    table = {
        k: fib4(k) for k in range(4, n+1)
    }

    # Compute the n-th element of the fib4 number sequence by adding the precomputed values
    return sum(table[k] for k in range(n-4, -1, -1))