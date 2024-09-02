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
    end = len(nums) - 1
    minSub = float('inf')
    minSubArray = []
    totalSum = sum(nums)

    while start < end:
        tempSum = nums[start] + nums[end]
        if tempSum < minSub:
            minSub = tempSum
            minSubArray = [nums[start], nums[end]]

        if tempSum >= 0:
            end -= 1
        else:
            start += 1

    return minSub, minSubArray

