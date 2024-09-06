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
    start, end = 0, 0
    curr_sum = 0

    while end < len(nums):
        curr_sum += nums[end]
        if curr_sum >= min_sum:
            curr_sum -= nums[start]
            start += 1

        min_sum = min(min_sum, curr_sum)
        end += 1
    return min_sum
