

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
    # fib4(0) -> 0
    # fib4(1) -> 0
    # fib4(2) -> 2
    # fib4(3) -> 0
    # fib4(4) -> 0
    # fib4(5) -> 4
    # fib4(6) -> 8
    # fib4(7) -> 14
    # fib4(8) -> 22
    # fib4(9) -> 34
    # fib4(10) -> 50
    # fib4(11) -> 74
    # fib4(12) -> 110
    # fib4(13) -> 164
    # fib4(14) -> 234
    # fib4(15) -> 324
    # fib4(16) -> 444
    # fib4(17) -> 620
    # fib4(18) -> 864
    # fib4(19) -> 1234
    # fib4(20) -> 1864
    # fib4(21) -> 2864
    # fib4(22) -> 4234
    # fib4(23) -> 6424
    # fib4(24) -> 9424

    def helper(n):
        a, b, c, d = 0, 2, 0, 0
        for _ in range(n):
            a, b, c, d = b, c, d, a + b + c + d
        return d

    return helper(n)

