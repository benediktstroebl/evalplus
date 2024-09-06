def double_the_difference(nums):
    """
    Sum of squares of odd integers in a list of numbers.
    
    Args:
        nums (list): List of numbers
    
    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains only negative integers or non-integer values.
    """
    result = 0
    for num in nums:
        if num > 0 and isinstance(num, int) and num % 2:
            result += num ** 2
    return result