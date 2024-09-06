def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Find the first Fibonacci number that is prime
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return a