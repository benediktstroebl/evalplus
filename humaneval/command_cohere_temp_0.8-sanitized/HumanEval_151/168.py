import unittest
def double_the_difference(numbers):
    """
    Sum the squares of odd numbers while ignoring negative or non-integer numbers.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        int: Sum of squares of odd numbers.
    
    """
    result = 0
    for num in numbers:
        if isinstance(num, int) and num >= 0:
            if num % 2:
                result += num ** 2

    return result