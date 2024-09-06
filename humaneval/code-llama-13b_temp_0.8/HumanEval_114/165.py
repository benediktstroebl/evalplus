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
        return

    window_sum, min_sum, window_start = 0, math.inf, 0
    for i in range(len(nums)):
        window_sum += nums[i]
        if window_sum < min_sum:
            min_sum = window_sum
            window_start = i

        if window_sum > 0:
            window_sum = 0
            i += 1

    if min_sum != math.inf:
        return min_sum

    return min(nums)

