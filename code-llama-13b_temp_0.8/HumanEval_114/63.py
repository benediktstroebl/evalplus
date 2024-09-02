import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # This is a brute force solution. It does not pass all test cases.
    min_sum = 9999999999
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for k in range(i, j):
                sum += nums[k]
            if sum < min_sum:
                min_sum = sum
    return min_sum
