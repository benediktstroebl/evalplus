import time
def double_the_difference(nums):
    """
    Sum of squares of odd integers in the list that are integers.
    
    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains only even or negative integers.
    """
    result = 0
    for num in nums:
        if num % 2 == 1 and num >= 0:
            result += num  * num
    return result
n = 10000
nums = [i for i in range(n)]