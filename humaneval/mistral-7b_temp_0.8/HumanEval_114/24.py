import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = float('inf')
    s = 0
    for i in range(len(nums)):
        s = s + nums[i]
        if i < len(nums) - 1:
            result = min(s, result)
        else:
            result = min(s, result)

    return result

