

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
    fibs = [0, 1, 2, 3]

    if n < 0:
        return 0

    if n <= 3:
        return fibs[n]

    count = 4
    while count <= n:
        fibs.append(fibs[-1] + fibs[-2] + fibs[-3] + fibs[-4])
        count += 1

    return fibs[n]

