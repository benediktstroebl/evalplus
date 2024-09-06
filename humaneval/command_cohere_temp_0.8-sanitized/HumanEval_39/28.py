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

    # Initialize two variables for the Fibonacci sequence
    a, b = 0, 1
    count = 0

    while count < n:
        # If a is prime, return it
        if is_prime(a):
            return a
        
        # Calculate the next number in the Fibonacci sequence
        a, b = b, a + b
        count += 1

    # If we reach this line, a is prime
    return a