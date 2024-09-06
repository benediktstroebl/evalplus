def largest_divisor(n):
    """
    Finds the largest divisor of n that is less than n.
    
    Args:
        n (int): Number to find the largest divisor of
    
    Returns:
        int: The largest divisor of n that is less than n
    """
    for i in range(1, n):
        if n % i == 0:
            return i