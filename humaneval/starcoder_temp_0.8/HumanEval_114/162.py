import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0

    min_sum = math.inf
    curr_sum = 0

    for i in range(0, len(nums)):
        curr_sum += nums[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return min_sum

