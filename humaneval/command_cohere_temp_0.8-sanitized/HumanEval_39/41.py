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
    Returns the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Initialize variables for the first and second terms of the Fibonacci sequence
    a, b = 0, 1
    
    # Generate the Fibonacci sequence, checking each number for primality
    for _ in range(n - 2):
        c = a + b
        if is_prime(c):
            return c
        a, b = b, c
    
    return None