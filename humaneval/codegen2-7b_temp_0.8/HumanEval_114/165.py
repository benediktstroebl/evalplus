import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums or len(nums) == 0:
        return 0
    sum_subarray = nums[0]
    minimum = sum_subarray
    for i in nums[1:]:
        sum_subarray = sum_subarray + i
        minimum = min(minimum, sum_subarray)
    return
