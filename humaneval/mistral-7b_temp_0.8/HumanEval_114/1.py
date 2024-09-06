import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return
    n = len(nums)
    start, sum_ = 0, 0
    min_ = math.inf
    for end in range(n):
        sum_ += nums[end]
        while sum_ > n:
            sum_ -= nums[start]
            start += 1
        min_ = min(min_, sum_)
    return min_
