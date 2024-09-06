import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = 0
    min_sum = math.inf
    for i in range(len(nums)):
        sum += nums[i]
        while sum < min_sum and i < len(nums):
            min_sum = sum
            i += 1
            if i < len(nums):
                sum += nums[i]
    return min_sum
