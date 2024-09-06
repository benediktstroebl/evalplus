def double_the_difference(nums):
    """
    Sum of squares of odd integers in a list given.
    
    Args:
        nums (list): List of numbers
    
    Returns:
        int: Sum of squares of odd integers or 0 if no such integers in the list
    """
    ans = 0
    for n in nums:
        if isinstance(n, int) and n > 0 and n % 2:
            ans += n * n
    return ans