import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) < 1:
        return 0
    start, end, sum = 0, 1, nums[0]
    while end < len(nums):
        if sum < 0:
            sum = nums[end]
            start = end
        else:
            sum += nums[end]
        end += 1
    return sum

