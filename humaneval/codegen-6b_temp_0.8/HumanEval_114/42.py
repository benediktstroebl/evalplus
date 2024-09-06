import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = nums[0]
    cumulative = 0
    for i, num in enumerate(nums):
        cumulative += num
        if cumulative < min_sum:
            min_sum = min(cumulative, min_sum)
        elif cumulative > min_sum:
            cumulative = 0

    return min_sum

