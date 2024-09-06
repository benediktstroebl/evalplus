import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float("inf")
    current_sum = 0
    start = 0
    end = 0
    for end, num in enumerate(nums):
        current_sum += num
        while current_sum >= 0:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[start]
            start += 1

    return min_sum
