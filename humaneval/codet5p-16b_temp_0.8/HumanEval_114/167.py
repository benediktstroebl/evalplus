import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 1:
        return nums[0]
    
    sum_min = math.inf
    
    for i in range(len(nums)):
        sum_min = min(sum_min, minSubArraySum(nums[i:]) + sum(nums[i:]))
    return sum_min
