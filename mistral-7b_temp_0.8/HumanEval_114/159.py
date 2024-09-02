import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = 2**32
    start = 0
    for end in range(len(nums)):
        while start < end and nums[start] > nums[end]:
            start += 1
        if end - start + 1 > 1:
            min_sum = min(min_sum, sum(nums[start:end+1]))
    return min_sum
