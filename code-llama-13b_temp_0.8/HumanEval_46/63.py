

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
    # Dummy base case
    if n <= 0:
        return 0
    # Init a list of all values computed so far
    fib4_seq = [0] * (n + 1)
    # Base case
    fib4_seq[0] = 0
    fib4_seq[1] = 0
    fib4_seq[2] = 2
    # Induction
    for i in range(3, n + 1):
        fib4_seq[i] = fib4_seq[i - 1] + fib4_seq[i - 2] + fib4_seq[i - 3] + fib4_seq[i - 4]
    return fib4_seq[n]

