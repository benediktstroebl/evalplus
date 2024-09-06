def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is positive
    n = abs(n)
    # Initialize two variables for the Fibonacci sequence
    x, y = 0, 1
    count = 0
    while count < n:
        # If x is prime, return it
        if is_prime(x):
            return x
        # Prepare the next number in the sequence
        y = x + y
        x = y
        count += 1
    # If we reach the end of the loop, return x
    return x