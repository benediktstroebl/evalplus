import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    low = 0
    low_sum = nums[0]
    for i in range(len(nums)):
        low_sum = low_sum + nums[i]
        if low_sum < nums[i]:
            low += 1
            low_sum = nums[i]
    
    if low_sum == 0:
        return nums[0]
    
