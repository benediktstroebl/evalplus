import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_so_far = math.inf
    total = 0
    for num in nums:
        total += num
        if total < min_so_far:
            min_so_far = total
    return min_so_far

