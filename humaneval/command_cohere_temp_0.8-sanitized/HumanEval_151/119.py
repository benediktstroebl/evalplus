def double_the_difference(nums):
    """
    Sum of squares of odd integers in a list of numbers.
    
    Args:
        nums (list): List of numbers
    
    Returns:
        int: Sum of squares of odd integers if positive integers are present, 
             returns 0 if negative numbers or non-integer numbers are present.
    """
    odd_integers = sum(x**2 for x in nums if x % 2 and x >= 0 and isinstance(x, int))
    return int(odd_integers * 2)