import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum, min_sum = nums[0], math.inf
    for num in nums[1:]:
        sum += num
        if sum < min_sum:
            min_sum = sum
        if sum < 0:
            sum = 0
    return min_sum
