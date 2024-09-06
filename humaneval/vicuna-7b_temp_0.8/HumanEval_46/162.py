

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
    # Fibonacci number fib(n) = fib(n-1) + fib(n-2)
    # We can represent the n-th number in the fib4 sequence as fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    # By solving the equation above we have fib4(n) = fib4(n-4) = fib4(n-5) = fib4(n-6) = 0
    # Thus we have fib4(n) = fib4(n-1) + fib4(n-2) = fib4(n-3) + fib4(n-4) = fib4(n-2) + fib4(n-3) = fib4(n-2) + fib4(n-3) = ... = fib4(n-2) + fib4(n-3) + fib4(n-4) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) = fib4(n-1) + fib4(n-2) = fib4(n-1) + fib4(n-3) = 0
    return 0