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
    curr_sum = 0
    l = len(nums)

    for i in range(l):
        curr_sum += nums[i]
        min_sum = min(min_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return min_sum
