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
    if n <= 1:
        return nums[0]
    result = math.inf
    min_sum = math.inf
    for i in range(n):
        min_sum = min(min_sum, nums[i])
        result = min(result, min_sum + sum(nums[i+1:]))

    return result




