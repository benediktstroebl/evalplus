import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = 0
    minSum = math.inf
    for right in range(len(nums)):
        sum = 0
        for i in range(left, right):
            sum += nums[i]
            if sum >= minSum:
                minSum = sum
        left = right + 1
    return min
