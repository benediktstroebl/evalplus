def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log n) time."""
    def fib(n: int) -> int:
        """Compute the n-th Fibonacci number inefficiently in O(n) time."""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    # Use the fact that the FibFib numbers and Fibonacci numbers overlap for n <= 8
    if n <= 8:
        return fib(n)
    # Use the fact that subsequent FibFib numbers are composed of three previous FibFib numbers
    else:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)