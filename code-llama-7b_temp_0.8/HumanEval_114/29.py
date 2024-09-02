import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # init
    n = len(nums)
    min_sum_right = 0
    min_sum_left = math.inf
    min_sum = math.inf
    # get the min_sum_left
    for i in range(n):
        if nums[i] < min_sum_left:
            min_sum_left = nums[i]
    # get the min_sum_right
    for i in range(n-1, -1, -1):
        if nums[i] < min_sum_right:
            min_sum_right = nums[i]
    # get the min_sum
    for i in range(n):
        min_sum = min(min_sum, min_sum_left + min_sum_right - nums[i])
    return min_sum
