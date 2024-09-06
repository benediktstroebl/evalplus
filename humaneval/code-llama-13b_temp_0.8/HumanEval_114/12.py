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
    min_sum = math.inf
    i = 0
    j = 0
    while i < n:
        while j < n and sum(nums[i:j+1]) < min_sum:
            j += 1
        if j != i:
            min_sum = sum(nums[i:j+1])
        i += 1
        j += 1
    return min_sum

