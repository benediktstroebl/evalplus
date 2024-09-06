import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    l = len(nums)
    start = 0
    end = 0
    sum = 0
    while end < l:
        if sum < 0:
            sum = 0
            start = end
        sum += nums[end]
        end += 1
    return sum
