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
    sum_ = 0
    min_ = nums[0]
    for num in nums:
        sum_ += num
        if min_ > sum_:
            min_ = sum_
        if sum_ < 0:
            sum_ = 0
    return min_
