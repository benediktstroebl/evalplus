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
    for i in nums:
        cur_sum += i
        min_sum = min(cur_sum, min_sum)
        if cur_sum < 0:
            cur_sum = 0

    return min_sum

