import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    total = 0
    min_start = 0
    min_end = 0
    min_sum = math.inf
    for i in range(length):
        total += nums[i]
        while(total > 0):
            min_sum = min(min_sum, total)
            total -= nums[min_end]
            min_end += 1
    return min_sum
