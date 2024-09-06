import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    start = 0
    runningSum = 0
    for end in range(len(nums)):
        runningSum += nums[end]
        while runningSum < 0 and start < end:
            runningSum -= nums[start]
            start += 1
        minSum = min(minSum, runningSum + nums[start])
    return minSum








