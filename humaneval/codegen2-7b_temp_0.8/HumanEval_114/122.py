import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = math.inf
    for i, num in enumerate(nums):
        if i > 0:
            sum -= nums[i-1]
        if sum > num:
            sum = num
    return sum
