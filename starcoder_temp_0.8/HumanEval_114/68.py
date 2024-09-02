import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    total = 0
    min_sum = math.inf
    start = 0
    for i in range(len(nums)):
        total += nums[i]
        while total >= 0:
            min_sum = min(min_sum, total)
            start += 1
            total -= nums[start - 1]
    return min_sum

