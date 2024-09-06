import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    start = 0
    end = 0
    while end < len(nums):
        if minSum > nums[end]:
            minSum = nums[end]
            start = end
        end += 1
    return minSum

