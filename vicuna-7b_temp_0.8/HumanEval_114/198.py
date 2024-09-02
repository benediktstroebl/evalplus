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
    result = []
    for i in range(1, len(nums)):
        right = nums[i]
        for j in range(i):
            right -= nums[j]
        if right == 0:
            continue
        if left - right + i > result[-1] + i:
            result.append(left - right + i)
    result.append(0)
    return result
