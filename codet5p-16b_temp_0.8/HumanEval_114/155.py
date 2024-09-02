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
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        while cur_sum >= min_sum:
            min_sum = min(min_sum, cur_sum - min_sum)
            cur_sum -= nums[i]

    return min_sum
