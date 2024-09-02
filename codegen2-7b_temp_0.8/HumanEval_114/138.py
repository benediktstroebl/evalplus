import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = float("inf")
    for i, v in enumerate(nums):
        sum = min(sum, v)
        if sum <= 0:
            sum = 0
        if i+1 == len(nums):
            break
        sum += nums[i+1]
    return sum
