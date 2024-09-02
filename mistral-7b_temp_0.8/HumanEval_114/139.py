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
        return 0

    l, r = 0, 0
    sum_ = 0
    min_ = math.inf

    while r < len(nums):
        sum_ += nums[r]
        while sum_ >= 0:
            sum_ -= nums[l]
            min_ = min(sum_, min_)
            l += 1
        r += 1
    return min_
