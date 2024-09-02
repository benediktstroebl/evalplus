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
        return 0
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        if nums[i] > 0:
            return min(minSubArraySum(nums[i:]), minSubArraySum(nums[:i]))
    return min(nums)
