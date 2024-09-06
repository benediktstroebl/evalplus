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
    limit = len(nums)
    minimum = nums[0]
    for i in range(0, limit):
        sum += nums[i]
        if (sum < 0):
            sum = 0
        if (sum < minimum):
            minimum = sum
            if (sum == 0):
                return 0

    return minimum
