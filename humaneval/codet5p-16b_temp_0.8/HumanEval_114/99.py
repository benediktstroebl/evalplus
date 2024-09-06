import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total_sum = 0
    minimum_sum = math.inf
    for i in range(len(nums)):
        total_sum += nums[i]
        for j in range(i, len(nums)):
            minimum_sum = min(minimum_sum, total_sum)
            total_sum -= nums[j]
    return minimum_sum

