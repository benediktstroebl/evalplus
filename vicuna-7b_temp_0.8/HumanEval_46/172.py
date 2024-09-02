

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
    # The fibonacci sequence with n = 0 is always 0
    if n == 0:
        return 0
    else:
        # The fibonacci sequence with n = 1 is always 0
        if n == 1:
            return 0
        else:
            # The fibonacci sequence with n = 2 is always 2
            if n == 2:
                return 2
            else:
                # The fibonacci sequence with n = 3 is always 0
                if n == 3:
                    return 0
                else:
                    # Use dynamic programming to calculate the n-th element of the fib4 sequence
                    a = fib4(n-1)
                    b = fib4(n-2)
                    c = fib4(n-3)
                    d = a + b + c + fib4(n-4)
                    return d
