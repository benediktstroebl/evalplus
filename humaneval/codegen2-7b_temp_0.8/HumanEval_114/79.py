import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = 0
    current_sum = 0
    min_sum = float("inf")
    for num in nums:
        current_sum += num
        max_sum = max(current_sum, max_sum)
        min_sum = min(current_sum, min_sum)
        if max_sum == min_sum:
            break
    return min_sum
