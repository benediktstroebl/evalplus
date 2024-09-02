import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # write your code here
    if len(nums) == 0:
        return 0

    i = 0
    sum = 0
    min_sum = 10**9
    while i < len(nums):
        sum += nums[i]
        if sum < min_sum:
            min_sum = sum
        if sum < 0:
            sum = 0
        i += 1
    return min_sum
