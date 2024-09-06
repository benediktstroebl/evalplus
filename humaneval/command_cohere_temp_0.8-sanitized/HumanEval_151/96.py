def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list that are integers.
    
    Args:
        nums (list): List of numbers.
    
    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains only even or negative numbers.
    """
    if not nums:  # Handle empty list
        return 0
    
    odd_nos = [num for num in nums if num % 2 and num >= 0]  # Filter odd, positive integers
    return sum(num ** 2 for num in odd_nos)