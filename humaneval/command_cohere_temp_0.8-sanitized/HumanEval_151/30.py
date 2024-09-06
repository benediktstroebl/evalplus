def double_the_difference(nums):
    """
    Sum of squares of odd integers in a list of numbers.
    
    Args:
        nums (list): List of numbers
    
    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains only negative integers or non-integer values.
    """
    result = 0
    for x in nums:
        if x > 0 and isinstance(x, int) and x % 2:
            result += x * x
    return result