import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums_sum = sum(nums)
    min_length = math.inf
    start = 0
    end = 0
    s = 0
    while end < len(nums):
        s += nums[end]
        end += 1
        while s >= nums_sum:
            min_length = min(min_length, end - start)
            s -= nums[start]
            start += 1
    return min_length
