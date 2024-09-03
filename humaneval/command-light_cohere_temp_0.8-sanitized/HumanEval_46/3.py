def fib4(n: int):
    """
    The Fibonacci sequence is defined as follows:
        fib4(0) -> 0
        fib4(1) -> 0
        fib4(2) -> 2
        fib4(3) -> 0
        fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """
    return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)