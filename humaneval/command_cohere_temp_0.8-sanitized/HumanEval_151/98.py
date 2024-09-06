import unittest
def double_the_difference(numbers):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    odd_numbers = [num for num in numbers if num % 2 != 0 and num >= 0]
    return sum(num ** 2 for num in odd_numbers)