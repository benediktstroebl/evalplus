import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    min_ = nums[0]
    max_ = nums[0]

    for i in range(1, n):
        max_ = max(max_ + nums[i], nums[i])
        min_ = min(min_ + nums[i], max_)

    return min_
