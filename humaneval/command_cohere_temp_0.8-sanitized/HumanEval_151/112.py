def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list that are integers.
    
    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains negative numbers.
    """
    result = 0
    for num in nums:
        if num % 2 != 0 and num >= 0:
            result += num ** 2
    return result