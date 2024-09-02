import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sub_sum = 0
    minimum = 0
    for i in range(len(nums)):
        sub_sum += nums[i]
        if minimum > sub_sum:
            minimum = sub_sum
        if sub_sum < 0:
            sub_sum = 0
    return minimum
