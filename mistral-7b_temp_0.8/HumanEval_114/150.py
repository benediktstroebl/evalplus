import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return
    if len(nums) == 1:
        return nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < res:
            res = nums[i]
        else:
            res += nums[i]
        if res < nums[i]:
            res -= nums[i]
    return res
