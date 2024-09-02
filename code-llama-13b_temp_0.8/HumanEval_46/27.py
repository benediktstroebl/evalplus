

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

    #
    # def fib4(n):
    #     if n <= 0:
    #         return 0
    #     fib4_1, fib4_2, fib4_3 = 0, 0, 2
    #     for i in range(3, n):
    #         fib4_4 = fib4_1 + fib4_2 + fib4_3
    #         fib4_1, fib4_2, fib4_3 = fib4_2, fib4_3, fib4_4
    #     return fib4_1 + fib4_2 + fib4_3
    #
    # return fib4(n)

    # if n <= 0:
    #     return 0
    #
    # i = 3
    #
    # last_last = 0
    # last = 0
    # cur = 2
    #
    # while i <= n:
    #     cur = last_last + last + cur
    #     last_last = last
    #     last = cur
    #     i += 1
    #
    # return cur

    def fib4(n):
        if n <= 0:
            return 0

        fib4_1, fib4_2, fib4_3 = 0, 0, 2
        for i in range(3, n + 1):
            fib4_4 = fib4_1 + fib4_2 + fib4_3
            fib4_1, fib4_2, fib4_3 = fib4_2, fib4_3, fib4_4

        return fib4_1 + fib4_2 + fib4_3

    return fib4(n)



