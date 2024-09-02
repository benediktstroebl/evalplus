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
    min_sub_array = math.inf
    for i,n in enumerate(nums):
        sum += n
        if sum < min_sub_array:
            min_sub_array = sum
        if sum < 0:
            sum = 0
    return min_sub_array

