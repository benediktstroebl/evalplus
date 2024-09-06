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
        return -math.inf
    res = nums[0]
    previous = nums[0]
    length = len(nums)
    for i in range(1, length):
        previous = max(previous + nums[i], nums[i])
        res = min(res, previous)
    return res

