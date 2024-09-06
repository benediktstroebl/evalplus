

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
    # Check if n is less than 4
    if n <= 3:
        # If n is less than 4, it's a trivial case, so we can return the answer directly
        return int(n)
    # Check if n is even
    if n % 2 == 0:
        # If n is even, we can use the formula fib4(n/2) = fib4(n/2-1) + fib4(n/2-2) to compute the answer
        return (fib4(n//2) + fib4(n//2-1)) + (fib4(n//2-1) + fib4(n//2-2))
    # Check if n is odd
    if n % 2 != 0:
        # If n is odd, we can use the formula fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) to compute the answer
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    
    
