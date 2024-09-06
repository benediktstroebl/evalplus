def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summation limit. Must be a positive integer.
    
    Returns:
        int: The sum if n is a positive integer, otherwise returns None.
    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return None
    
    return sum(range(1, n + 1))