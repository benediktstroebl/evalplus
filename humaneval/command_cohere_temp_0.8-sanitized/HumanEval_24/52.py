def largest_divisor(n):
    """
    Finds the largest divisor of n less than n itself.
    
    Args:
        n (int): Number to find the largest divisor for
    
    Returns:
        int: Largest divisor of n
    """
    for i in range(1, n):
        if n % i == 0:
            return i