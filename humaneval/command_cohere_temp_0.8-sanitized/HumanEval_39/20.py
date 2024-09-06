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
    
    # Initialize variables for the first and second Fibonacci numbers
    a, b = 0, 1
    
    # Iterate through the Fibonacci sequence to find the n-th prime number
    for i in range(n - 1):
        a, b = b, a + b
        
        # Check if the current number is prime
        if is_prime(a):
            return a
    
    return None