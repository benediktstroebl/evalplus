def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summates integers up to this value.
        
    Returns:
        int: Sum of integers from 1 to n.
    """
    return n * (n + 1) // 2  # Sum of integers from 1 to n is n(n+1)/2