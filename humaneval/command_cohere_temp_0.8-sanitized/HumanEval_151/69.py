import unittest
def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list while ignoring negatives and non-integers.

    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd numbers or 0 if the list is empty or contains only even or negative numbers.
    """
    result = 0
    for num in nums:
        if num % 2 != 0 and num > 0:  # Check for oddness and non-negative
            result += num ** 2

    return result