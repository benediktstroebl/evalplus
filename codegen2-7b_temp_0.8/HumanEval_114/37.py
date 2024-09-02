import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_ = 0
    start = end = 0
    min_ = math.inf
    for end in range(len(nums)):
        sum_ += nums[end]
        while sum_ >= nums[start]:
            min_ = min(min_, sum_ - nums[start])
            start += 1
        sum_ -= nums[end]
    return
