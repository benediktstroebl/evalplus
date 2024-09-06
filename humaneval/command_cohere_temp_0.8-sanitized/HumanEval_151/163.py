import unittest
def double_the_difference(numbers):
    """
    Sum of squares of odd numbers in the list while ignoring negatives and non-integers.

    Args:
        numbers (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if input list is empty.
    """
    result = 0
    for num in numbers:
        if num % 2 == 0 and num >= 0 and isinstance(num, int):
            result += num ** 2

    return result