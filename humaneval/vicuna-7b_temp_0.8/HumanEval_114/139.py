import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = nums[0]
    right = nums[-1]
    result = 0
    
    for i in range(1, len(nums)):
        if nums[i] >= right:
            left += nums[i]
        else:
            result = max(result, left - nums[i])
            left = nums[i]
    
    return result
