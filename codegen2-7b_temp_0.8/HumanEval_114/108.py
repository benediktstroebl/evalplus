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
    sum_so_far = 0
    for i in range(len(nums)):
        sum_so_far += nums[i]
        if sum_so_far < min_sum:
            min_sum = sum_so_far
    return min_sum if min_sum!= math.inf else 0
