import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = 0
    min_sum = math.inf
    for i in range(0, len(nums)):
        if i == 0:
            sum += nums[i]
            min_sum = sum
            continue
        sum = sum + nums[i]
        if sum < min_sum:
            min_sum = sum
    return min_sum
