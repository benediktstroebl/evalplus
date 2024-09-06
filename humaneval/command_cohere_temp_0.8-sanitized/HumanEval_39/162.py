def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Ensure n is a positive integer
    n = abs(int(n))
    if n <= 0:
        return None

    # Initialize variables for the first and second Fibonacci numbers
    a, b = 0, 1
    count = 0

    while count < n:
        # Calculate the next Fibonacci number
        c = a + b
        a, b = b, c

        # Check if the calculated number is prime
        if is_prime(c):
            count += 1

    # Return the expected Fibonacci number
    return b