import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    res = float('-inf')
    for i in range(len(nums)):
        for j in range(i):
            for k in range(len(nums)):
                if i < k:
                    if nums[i] + nums[j] + nums[k] == res:
                        res = min(res, nums[i] + nums[j] + nums[k])
    return res
