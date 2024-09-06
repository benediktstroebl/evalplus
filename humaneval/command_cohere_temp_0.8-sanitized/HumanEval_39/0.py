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
    Generates the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    
    # Generate and filter candidates up to the n-th Fibonacci number
    for i in range(max(5000, 2 * n), 0, -1):
        # Check if the current number is prime
        if is_prime(i):
            # Check if the number is part of the Fibonacci sequence
            if i == a or i == b:
                return i
            a, b = b, a + b
    
    return None