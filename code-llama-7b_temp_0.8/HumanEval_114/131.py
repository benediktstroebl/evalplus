import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minimum = 0
    window_min = math.inf
    window_sum = 0

    for num in nums:
        window_sum += num
        window_min = min(window_min, window_sum)
        minimum = min(window_min, minimum)

    return minimum
