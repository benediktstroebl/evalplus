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
    sub_sum = math.inf
    left = 0
    for right, n in enumerate(nums):
        sum += n
        if sum < sub_sum:
            sub_sum = sum
            left = left + 1
    return sum
