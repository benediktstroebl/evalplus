

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
    if n < 0:
        raise RuntimeError("Invalid input.")
    if n <= 3:
        return 0

    # The following loop computes Fib(n) using the following formula:
    #   fib(n) = fib(n-1) + fib(n-2) + fib(n-3) + fib(n-4)
    # It works by storing the values for the previous 4 calls in a list
    # the nth call will return (fib(n-1) + fib(n-2) + fib(n-3) + fib(n-4))

    prev_fibs = [0, 0, 2, 0]
    for i in range(4, n+1):
        new_val = prev_fibs[0] + prev_fibs[1] + prev_fibs[2] + prev_fibs[3]
        prev_fibs[0] = prev_fibs[1]
        prev_fibs[1] = prev_fibs[2]
        prev_fibs[2] = prev_fibs[3]
        prev_fibs[3] = new_val
    return prev_fibs[3]


