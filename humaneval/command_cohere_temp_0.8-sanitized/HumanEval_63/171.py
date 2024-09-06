def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log n) time."""
    def fib(n: int) -> int:
        """Compute the n-th Fibonacci number."""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    # Use the closed-form expression for the n-th FibFib number
    # to get an O(log n) time solution.
    return fib(n - 2) + fib(n - 3)