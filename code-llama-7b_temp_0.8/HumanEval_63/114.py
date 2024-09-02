

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    a, b = 0, 1
    if n < 1:
        return a
    elif n < 2:
        return b
    elif n < 3:
        return a + b

    fib_fib_list = [a, b, a+b]
    n -= 3
    while n:
        fib_fib_list.append(fib_fib_list[-1] + fib_fib_list[-2] + fib_fib_list[-3])
        n -= 1
    return fib_fib_list[-1]

