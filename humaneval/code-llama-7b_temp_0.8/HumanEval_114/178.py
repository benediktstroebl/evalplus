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
    min_sum_start = 0
    min_sum_end = 0
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        # if we are under the min sum so far, update it
        if curr_sum < min_sum:
            min_sum = curr_sum
            min_sum_start = i
            min_sum_end = i
        # if we are the same as the min sum, update it, since we have a shorter range
        elif curr_sum == min_sum:
            min_sum_end = i

        # if the sum is negative, reset it
        elif curr_sum < 0:
            curr_sum = 0

    return min_sum, nums[min_sum_start : min_sum_end+1]
