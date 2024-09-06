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
    min_sum = math.inf
    sum_ = 0

    for i, n in enumerate(nums):
        sum_ += n
        while sum_ < 0:
            sum_ -= nums[start]
            start += 1
        min_sum = min(min_sum, sum_)

    return 0 if min_sum == math.inf else min_sum

