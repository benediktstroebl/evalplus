import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    res = nums[0]
    for i in range(1, n):
        for j in range(i+1, n):
            if nums[i] + nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                res = max(res, nums[i] + nums[j])
    return res
