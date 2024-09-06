import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    curr_sum = 0
    min_sub = float('inf')
    head = 0
    tail = 0
    while tail < len(nums):
        curr_sum += nums[tail]
        while head <= tail and curr_sum >= 0:
            min_sub = min(min_sub, curr_sum)
            curr_sum -= nums[head]
            head += 1
        tail += 1
    return min_sub
