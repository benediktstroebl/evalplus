import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]

    total = 0
    min_total = float('inf')
    start = 0
    end = 0
    while end < len(nums):
        total += nums[end]
        end += 1
        while total >= 0:
            min_total = min(min_total, total)
            total -= nums[start]
            start += 1

    if min_total == float('inf'):
        return 0
    return min_total
