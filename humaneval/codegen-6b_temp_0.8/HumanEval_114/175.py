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
    current_sum = 0
    for i in range(n):
        current_sum = current_sum + nums[i]
        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum
