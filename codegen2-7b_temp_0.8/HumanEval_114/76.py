import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    ret = float('inf')
    sum = 0
    for num in nums:
        sum += num
        if sum < ret:
            ret = sum
        if sum > 0:
            sum = sum - num
    return ret if ret!= float('inf') else
