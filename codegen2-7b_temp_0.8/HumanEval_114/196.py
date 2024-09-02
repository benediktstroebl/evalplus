import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    s = 0
    left = 0
    total = 0
    min_sum = math.inf
    for right, num in enumerate(nums):
        total += num
        while left <= right and total >= s:
            min_sum = min(min_sum, total - s)
            left += 1
            s += num
    return min_sum
