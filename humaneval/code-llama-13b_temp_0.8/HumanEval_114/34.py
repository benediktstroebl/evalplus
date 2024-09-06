import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    window_sum = 0
    window_start = 0

    for window_end in range(len(nums)):
        window_sum += nums[window_end]
        min_sum = min(min_sum, window_sum)

        while window_sum < 0 and window_start < len(nums) - 1:
            window_sum += nums[window_start]
            window_start += 1
            min_sum = min(min_sum, window_sum)

    return min_sum

