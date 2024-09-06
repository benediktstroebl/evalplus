def fib(n):
    """Return n-th Fibonacci number."""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)