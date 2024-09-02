import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    target = sum(nums)
    start = 0
    end = 0
    min_sum = math.inf
    while end < len(nums):
        curr_sum = sum(nums[start:end+1])
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum >= target:
            end += 1
        else:
            start +=
