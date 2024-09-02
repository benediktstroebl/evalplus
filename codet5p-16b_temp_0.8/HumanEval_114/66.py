import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    running_sum = 0
    window_start = 0
    window_end = 0
    min_sum = math.inf
    for window_end in range(len(nums)):
        running_sum += nums[window_end]
        while running_sum >= nums[window_start]:
            min_sum = min(min_sum, running_sum - nums[window_start])
            window_start += 1
    return min_sum
