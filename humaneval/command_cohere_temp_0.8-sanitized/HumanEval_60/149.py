def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Sum ends at nFh, inclusive. Must be a positive integer.
    
    Returns:
        int: The sum of integers from 1 to n.
    """
    # Calculate the sum
    sum_n = 0
    for num in range(1, n+1):
        sum_n += num
    return sum_n