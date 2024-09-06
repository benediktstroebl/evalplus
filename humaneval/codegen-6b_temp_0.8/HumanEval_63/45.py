

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
    # t1, t2, t3 = 0, 1, 1
    # for i in range(3, n + 1):
    #     t3 = t1 + t2
    #     t1 = t2
    #     t2 = t3
    # return t3

    #t1, t2 = 0, 1
    #for i in range(3, n + 1):
    #    t3 = t1 + t2
    #    t1, t2 = t2, t3
    # return t1

    # t, i = 0, 0
    # while i < n:
    #     t, i = t + i, i + 1
    # return t
    # return 1 if n <= 1 else fibfib(n-1) + fibfib(n-2)
    # if n < 2:
    #     return n
    # t1, t2 = 0, 1
    # for _ in range(n - 1):
    #     t1, t2 = t2, t1 + t2
    # return t2
    # return fibfib(n - 1) + fibfib(n - 2)
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # t = 0
    # for i in range(2, n + 1):
    #     t += 1
    # return t

    count, t1, t2 = 0, 0, 1
    while count < n:
        t1, t2 = t2, t1 + t2
        count += 1
    return t2
