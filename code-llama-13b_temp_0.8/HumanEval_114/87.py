import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    m = math.inf
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        if i == len(nums) - 1 or total > nums[i + 1]:
            if m > total:
                m = total
            total = 0
    return m

