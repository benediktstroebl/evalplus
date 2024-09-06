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
        return -1

    min_sum = float('inf')
    min_start = 0
    sum = 0
    for i, n in enumerate(nums):
        sum += n
        if sum < min_sum:
            min_sum = sum
            min_start = i
    return min_sum if sum > 0 else -1
