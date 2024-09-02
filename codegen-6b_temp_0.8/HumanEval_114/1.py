import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total, min_subarray = nums[0], nums[0]
    for num in nums[1:]:
        total += num
        min_subarray = min(min_subarray, total)
    return min_subarray
