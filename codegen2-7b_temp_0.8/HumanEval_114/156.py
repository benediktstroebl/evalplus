import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float("inf")
    for i in range(len(nums)):
        if i == 0:
            continue
        sum = nums[i]
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum < min_sum:
                min_sum = sum
    return min_
