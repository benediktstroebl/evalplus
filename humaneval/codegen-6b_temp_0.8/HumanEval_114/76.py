import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    start = 0
    cur_sum = 0
    min_sum = math.inf
    for i in range(length):
        cur_sum += nums[i]
        while cur_sum >= 0:
            min_sum = min(min_sum, cur_sum)
            cur_sum -= nums[start]
            start += 1
    return min_sum

