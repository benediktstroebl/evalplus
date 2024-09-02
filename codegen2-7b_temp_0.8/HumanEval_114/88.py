import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    global max_sum, min_sum
    max_sum = min_sum = float("inf")
    global sum_found, start, end
    sum_found = 0
    start = 0
    end = -1

    for i in range(0, len(nums)):
        sum_found += nums[i]

        if sum_found < min_sum:
            min_sum = sum
