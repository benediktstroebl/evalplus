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
    min_sum = nums[0]
    sum_ = 0
    for i in range(len(nums)):
        sum_ += nums[i]
        if min_sum > sum_:
            min_sum = sum_
        if sum_ < 0:
            sum_ = 0
    return min_sum

