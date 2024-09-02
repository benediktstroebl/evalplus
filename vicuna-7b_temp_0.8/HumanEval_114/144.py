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
    min_sum = math.inf
    for i in range(1, n):
        for j in range(i):
            if nums[i] + nums[j] < nums[i]:
                min_sum = min(min_sum, nums[i] + nums[j])
    return min_sum