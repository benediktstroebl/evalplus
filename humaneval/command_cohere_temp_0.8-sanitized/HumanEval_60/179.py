def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): The highest number to be included in the sum.
        
    Returns:
        int: The sum of integers from 1 to n.
    """
    return n * (n + 1) // 2  # Sum formula for pairs of integers