import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = 0
    sum = 0
    min_value = float("inf")
    for i in nums:
        total += i
        sum += i
        if sum < min_value:
            min_value = sum
        elif sum > min_value:
            min_value = sum - min_value
        if sum < 0:
            sum = 0
    return min_
