import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums == None or len(nums) == 0:
        return 0

    minSum = nums[0]
    runningSum = nums[0]
    for i in range(1, len(nums)):
        runningSum = min(runningSum+nums[i], nums[i])
        minSum = min(minSum, runningSum)
    return minSum

