def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is a positive integer
    n = abs(int(n))
    if n == 0:
        return 1 # First number is 1 and it's prime as well
    elif n == 1:
        return 2 # Second number is 2 and it's prime as well
    # Initialize two variables for the Fibonacci sequence
    a, b = 0, 1
    for _ in range(n - 1):
        # Each iteration gives the next Fibonacci number
        a, b = b, a + b
    # Finally, return the n-th Fibonacci number
    return a