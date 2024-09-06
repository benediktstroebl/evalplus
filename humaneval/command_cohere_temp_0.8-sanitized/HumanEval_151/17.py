def double_the_difference(nums):
    """
    Sum of squares of odd integers from the list of numbers.
    
    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains only even or negative numbers.
    """
    assert isinstance(nums, list), "Input 'nums' must be a list."
    assert all(isinstance(num, int) for num in nums), "Input 'nums' must contain only integers."
    assert all(num >= 0 for num in nums), "Input 'nums' must not contain negative numbers."

    odd_squares = sum(num ** 2 for num in nums if num % 2 == 1 and num != 0)
    return int(odd_squares)