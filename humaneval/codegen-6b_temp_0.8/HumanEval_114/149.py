import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    start = 0
    end = 0
    min_sum = float('inf')
    sums = 0

    for i in range(0,len(nums)):
        sums += nums[i]
        while sums < 0:
            sums = sums - nums[start]
            start += 1

        if sums < min_sum:
            min_sum = sums
            end = i

    return min_sum
