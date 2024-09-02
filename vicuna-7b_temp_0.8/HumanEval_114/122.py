import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    min_sum = nums[0]
    for i in range(1, n):
        sub_sum = 0
        for j in range(i):
            sub_sum += nums[j]
        if sub_sum > min_sum:
            return sub_sum
        else:
            min_sum = sub_sum
    return min_sum
