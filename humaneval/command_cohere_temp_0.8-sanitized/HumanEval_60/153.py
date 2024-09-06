def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summation limit.
    
    Returns:
        int: The sum if n is a positive integer, otherwise returns None.
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum