import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSums = {0: -1}
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]
        if total in minSums:
            continue
        minSums[total] = i
    return min(minSums.values())
