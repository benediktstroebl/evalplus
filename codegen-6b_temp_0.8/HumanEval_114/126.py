import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = min(nums)
    subArr_sum = nums[0]
    max_sum = nums[0]
    for i in range(1,len(nums)):
        subArr_sum = max(subArr_sum + nums[i], nums[i])
        if subArr_sum < min_sum: min_sum = subArr_sum
        if subArr_sum > max_sum: max_sum = subArr_sum
    return min_sum
