import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    min = float("inf")
    curr = 0
    for num in nums:
        curr = curr + num
        if curr < min:
            min = curr
        if curr < 0:
            curr = 0
    return min
