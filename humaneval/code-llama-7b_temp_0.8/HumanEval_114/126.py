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
    min_sum = float("inf")
    sum_so_far = 0
    i = 0

    while i < n:
        while sum_so_far > 0 and i < n:
            sum_so_far += nums[i]
            if sum_so_far < min_sum:
                min_sum = sum_so_far
            i += 1

        while i < n:
            sum_so_far += nums[i]
            if sum_so_far < 0:
                break
            if sum_so_far < min_sum:
                min_sum = sum_so_far
            i += 1
        sum_so_far = 0
    return min_sum

