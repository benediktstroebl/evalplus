import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = float('inf')
    min_sum = float('inf')
    for i in nums:
        sum += i
        if sum < min_sum:
            min_sum = sum
    return min_sum if min_sum!= float('inf') else sum

