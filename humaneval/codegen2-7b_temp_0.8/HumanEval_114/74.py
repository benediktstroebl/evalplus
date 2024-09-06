import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    sum_ = 0
    for num in nums:
        sum_ += num
        if sum_ < min_sum:
            min_sum = sum_
        if sum_ >= 0:
            sum_ = 0
    return min_
