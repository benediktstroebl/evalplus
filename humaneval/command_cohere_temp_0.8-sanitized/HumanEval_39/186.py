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
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Initialize first two fibonacci numbers
    a, b = 0, 1
    count = 3

    while count < n:
        # Calculate next fibonacci number
        c = a + b
        a, b = b, c

        # Check if it's a prime
        if is_prime(b):
            count += 1

    return b