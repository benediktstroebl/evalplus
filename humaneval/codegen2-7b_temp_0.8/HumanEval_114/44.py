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
        return -1
    if len(nums) == 1:
        return nums[0]
    return nums[0] + min(nums[1:]) if sum(nums[1:]) < sum(nums[:1]) else minSubArraySum(nums[1:
