def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Initialize two variables for the first two fibonacci numbers
    a, b = 0, 1
    count = 0

    while True:
        # Check if the current number is prime
        if is_prime(a):
            count += 1

        # Return the Fibonacci number if it's the n-th prime Fibonacci number
        if count == n:
            return a

        # Calculate the next Fibonacci number
        a, b = b, a + b