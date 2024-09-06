import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    best_s = math.inf
    curr_s = 0
    for i in range(len(nums)):
        curr_s += nums[i]
        while curr_s > best_s:
            curr_s -= nums[i - len(nums)]
        if curr_s < best_s:
            best_s = curr_s
    return best_s
