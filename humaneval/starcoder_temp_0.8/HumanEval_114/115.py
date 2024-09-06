import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # this is the same as finding the largest sub array, but this is the sum
    # of that subarray
    sum_ = 0
    smallest_sum = float('inf')
    for num in nums:
        sum_ += num
        smallest_sum = min(sum_, smallest_sum)
        if sum_ < 0:
            sum_ = 0
    return smallest_sum
