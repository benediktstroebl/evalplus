import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = float("inf")
    min_sum = float("inf")
    start = 0
    for end in range(len(nums)):
        sum += nums[end]
        if sum >= min_sum:
            min_sum = sum
        while sum >= 0:
            sum -= nums[start]
            start += 1
            if sum < min_sum:
                min_sum =
