import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    n = len(nums)
    curr_sum = 0
    min_sum = math.inf
    for i in range(0, n):
        curr_sum += nums[i]
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum < min_sum:
            min_sum = curr_sum
    if min_sum == math.inf:
        return 0
    return min_sum
