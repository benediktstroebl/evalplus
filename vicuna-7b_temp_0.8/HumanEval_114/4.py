import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = max(nums)
    right = sum(nums)
    result = [left]
    for i in range(1, len(nums)):
        right = sum(nums[:i]) - nums[i]
        if right >= 0:
            result.append(right)
    return result
