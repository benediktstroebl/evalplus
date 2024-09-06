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
    high = 0
    max_sum = 0
    while high < len(nums):
        max_sum = max(max_sum, nums[high])
        while low < len(nums) and max_sum >= nums[low]:
            low += 1
        high += 1
    return min(max_sum, nums[low]
