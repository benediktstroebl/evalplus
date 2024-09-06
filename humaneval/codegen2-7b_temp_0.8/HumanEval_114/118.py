import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float("inf")
    sum_ = 0
    for num in nums:
        if sum_ < 0:
            sum_ = 0
        sum_ += num
        min_sum = min(min_sum, sum_)

    return min_sum if min_sum!= float("inf") else 0
