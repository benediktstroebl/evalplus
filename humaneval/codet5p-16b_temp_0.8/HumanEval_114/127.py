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
    min_sum = math.inf
    start = 0
    for end in range(len(nums)):
        sum_ += nums[end]
        while sum_ >= 0:
            min_sum = min(min_sum, sum_)
            sum_ -= nums[start]
            start += 1
    return min_sum

