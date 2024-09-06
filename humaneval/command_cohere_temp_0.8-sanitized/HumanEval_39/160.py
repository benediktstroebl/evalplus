def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    prev, curr = 0, 1
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr