def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list, while ignoring negatives and non-integers.

    :param nums: List of numbers.
    :return: Sum of squares of odd integers or 0 if the list is empty.
    """
    assert isinstance(nums, list), "Input should be a list."
    
    odd_squares = sum(x**2 for x in nums if x % 2 and x >= 0 and isinstance(x, int))
    return int(odd_squares)