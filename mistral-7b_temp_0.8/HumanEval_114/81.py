import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = nums[0]
    sum = nums[0]
    for i in range(1, len(nums)):
        sum = sum + nums[i]
        if sum > nums[i]:
            sum = nums[i]
            min_sum = sum
        if sum < min_sum:
            min_sum = sum
    return min_sum
