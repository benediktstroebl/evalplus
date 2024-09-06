import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSubArray = nums[0]
    total = 0

    for x in nums:
        total = total + x

        if total < minSubArray:
            minSubArray = total

    return minSubArray

