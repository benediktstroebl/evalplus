import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum, curr_sum, start, end = float('inf'), 0, 0, 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum >= 0:
            min_sum = min(min_sum, curr_sum)
            if min_sum == 0:
                return min_sum
        if curr_sum < 0:
            if min_sum == float('inf'):
                return min_sum
            curr_sum = 0
            start = i + 1
    return min_sum
