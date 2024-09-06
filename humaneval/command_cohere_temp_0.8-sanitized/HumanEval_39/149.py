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
    Generates the n-th Fibonacci number that is also prime
    """
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Start with the first two Fibonacci numbers
    a, b = 0, 1
    count = 3

    while not is_prime(a) or not is_prime(b):
        # Calculate the next Fibonacci number
        a, b = b, a + b
        
        # Increment count if both numbers are prime
        if is_prime(a) and is_prime(b):
            count += 1
        
        # Check if we've generated enough Fibonacci numbers
        if count == n:
            return b
    
    return None