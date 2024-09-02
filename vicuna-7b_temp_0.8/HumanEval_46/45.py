

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
    if n < 0 or n > 4:
        raise ValueError("Invalid index")
    elif n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 0
    else:
        a, b, c, d = fibonacci(n-1), fibonacci(n-2), fibonacci(n-3), fibonacci(n-4)
        return a + b + c + d
