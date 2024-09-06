import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float('inf')
    left_sum = 0
    for right_sum in range(len(nums)):
        left_sum += nums[right_sum]
        print(left_sum)
        if left_sum < min_sum:
            min_sum = left_sum
        if left_sum > 0:
            left_sum -= nums[right_sum]
