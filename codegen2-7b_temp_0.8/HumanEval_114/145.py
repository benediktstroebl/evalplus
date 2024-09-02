import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    start = 0
    end = 0
    sum = 0
    while end < len(nums):
        sum += nums[end]
        end += 1
        while sum >= nums[start]:
            sum -= nums[start]
            start += 1
        if sum == 0:
            return sum

