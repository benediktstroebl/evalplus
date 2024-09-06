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
    if n <= 0:
        raise ValueError("n must be positive")
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    count = 0

    while count < n:
        # Compute the next Fibonacci number
        c = a + b
        a, b = b, c

        # Check if the Fibonacci number is prime
        if is_prime(c):
            count += 1

    return c