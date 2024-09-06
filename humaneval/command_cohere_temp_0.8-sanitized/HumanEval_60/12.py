def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summation limit.
    
    Returns:
        int: The sum if n is a positive integer, otherwise returns None.
    """
    if not isinstance(n, int) or n < 1:
        return None
    return sum(range(1, n + 1))