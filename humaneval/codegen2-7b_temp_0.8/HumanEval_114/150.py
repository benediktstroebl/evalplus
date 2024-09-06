import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = sum(nums)
    if total == 0: return 0
    cur_min, cur_sum, start, end = float('inf'), 0, 0, 0
    while end < len(nums):
        cur_sum += nums[end]
        if cur_sum < cur_min:
            cur_min = cur_sum
        while cur_sum >= total:
            cur_sum -= nums[start]
            start +=
