import unittest
def double_the_difference(numbers):
    """
    Sum of squares of odd numbers in the list while ignoring negatives and non-integers.

    Returns 0 if the list is empty.
    """
    result = 0
    for num in numbers:
        if num % 2 != 0 and num >= 0 and isinstance(num, int):
            result += num ** 2

    return result