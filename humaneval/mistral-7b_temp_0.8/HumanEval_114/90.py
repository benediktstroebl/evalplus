import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = 99999
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            curr = 0
            for k in range(i, j+1):
                curr += nums[k]
            if min_sum > curr:
                min_sum = curr
    return min_sum

