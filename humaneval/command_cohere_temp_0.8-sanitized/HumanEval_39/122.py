def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is positive
    n = abs(n)
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Start with the 3rd Fibonacci number (2nd is 1, which is not prime)
        a, b = 3, 5
        for _ in range(n - 2):
            a, b = b, a + b
        return a