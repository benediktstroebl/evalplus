import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = nums[0]
    min_sum = sum
    for i in range(1, len(nums)):
        sum += nums[i]
        if sum < nums[i]:
            min_sum = min(min_sum, sum)
            sum = nums[i]
    return min_sum
