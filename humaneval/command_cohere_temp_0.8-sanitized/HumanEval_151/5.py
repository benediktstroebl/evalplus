def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list, ignoring negatives and non-integers.
    
    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if input list is empty or contains only negatives or non-integers.
    """
    result = 0
    for num in nums:
        if num > 0 and isinstance(num, int) and num % 2:
            result += num ** 2

    return result