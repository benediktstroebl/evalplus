

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
    # fibonacci with a list to store the previous results
    fib4s = [0, 0, 2, 0]
    if n == 0 or n == 1 or n == 2 or n == 3:
        return fib4s[n]
    for i in range(4, n+1):
        fib4s.append(fib4s[i-1] + fib4s[i-2] + fib4s[i-3] + fib4s[i-4])
    return fib4s[n]

