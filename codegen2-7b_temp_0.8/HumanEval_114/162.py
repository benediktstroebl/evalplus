import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    min_sum = float('inf')
    temp_sum = 0
    for i in range(len(nums)):
        temp_sum += nums[i]
        if temp_sum < min_sum:
            min_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0
    return min_sum
