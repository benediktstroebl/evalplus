

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

    # Define the function
    def fib4(n: int) -> int:
        # Check if n is 0 or 1
        if n == 0 or n == 1:
            return n
        # Check if n is even or odd
        if n % 2 == 0:
            # Use fib4 to compute the left half of n
            return fib4(n // 2) + fib4(n // 2 + 1)
        else:
            # Use fib4 to compute the right half of n
            return fib4(n // 2) - fib4(n // 2 + 1)

    # Test the function
    assert fib4(5) == 4, "fib4(5) should be 4"
    assert fib4(6) == 8, "fib4(6) should be 8"
    assert fib4(7) == 14, "fib4(7) should be 14"
