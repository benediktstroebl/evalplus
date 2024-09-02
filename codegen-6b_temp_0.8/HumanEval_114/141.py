import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    for i in range(len(nums)):
        aux = 0
        for j in range(i, len(nums)):
            aux += nums[j]
            min_sum = min(aux, min_sum)
    return min_sum
