import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0

    min_sum = nums[0]
    size = len(nums)
    for i in range(size):
        min_sum -= nums[i]
        min_sum = min(min_sum, min_sum + nums[i+1])
    return min_sum

