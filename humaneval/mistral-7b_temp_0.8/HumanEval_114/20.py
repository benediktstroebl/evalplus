import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    sum = 0
    start = 0

    for i in range(len(nums)):
        sum = sum + nums[i]
        if i == 0:
            min_sum = sum
        else:
            if sum < min_sum:
                min_sum = sum
        if sum < 0:
            start = i+1
            sum = 0
    return min_sum
