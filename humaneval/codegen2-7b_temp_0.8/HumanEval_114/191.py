import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    min_sum = math.inf
    min_start = 0
    for i in range(len(nums)):
        sum_now = sum(nums[i:])
        if sum_now < min_sum:
            min_sum = sum_now
            min_start = i
    return min_sum
