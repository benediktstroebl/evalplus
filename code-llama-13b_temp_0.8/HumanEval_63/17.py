

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
    if n < 0:
        return None
    if n in [0, 1]:
        return 0

    # if n is odd, then last digit is 0
    # if n is even, then last digit is 4
    last_digit = n % 2

    # compute (n // 2) + (n // 2) + 1
    # this is also the number of elements in FibFib(n)
    FibFib_len = (n // 2) + (n // 2) + 1

    # compute Fibonacci(FibFib_len)
    a = 0
    b = 1
    for _ in range(FibFib_len - 1):
        a, b = b, a + b

    # compute FibFib(n)
    # if n is odd, then the result is FibFib(n // 2)
    # if n is even, then the result is (FibFib(n // 2) + FibFib(n // 2 - 1)) % 10
    if last_digit == 1:
        return (a + b) % 10
    else:
        return (a + b - 1) % 10

