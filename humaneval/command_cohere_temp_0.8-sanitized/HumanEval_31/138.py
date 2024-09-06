def is_prime(n):
    """
    Checks whether a given number is prime.
    
    Args:
        n (int): Number to check for primality.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True