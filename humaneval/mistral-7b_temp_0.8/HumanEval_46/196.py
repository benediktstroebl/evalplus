

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
    #your code here
    if n == 0 or n == 1 or n == 2:
        return 0
    if n == 3:
        return 2
    x = [0,0,0,2]
    if n >= 4:
        for i in range(4,n):
            x[i] = x[i-1] + x[i-2] + x[i-3] + x[i-4]
    return x[n]
