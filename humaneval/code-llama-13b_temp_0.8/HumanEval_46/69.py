

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

    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    previous_2 = 0
    previous_1 = 0
    current = 2
    # At this point, current = fib4(3)
    for _ in range(4, n):
        # At this point, current = fib4(i), where i is between 4 and n - 1
        # We need to compute fib4(i + 1) = fib4(i) + fib4(i-1) + fib4(i-2) + fib4(i-3)

        # The following is the key to solving this problem.  We'll come back to this after the code is written.
        temp = current + previous_2 + previous_1

        # At this point, temp = fib4(i) + fib4(i-1) + fib4(i-2) + fib4(i-3)
        # However, the following assignment statement will compute fib4(i + 1) = fib4(i) + fib4(i-1) + fib4(i-2) + fib4(i-3)

        previous_2 = previous_1  # fib4(i-3)
        previous_1 = current  # fib4(i-2)
        current = temp  # fib4(i-1)

    return current

