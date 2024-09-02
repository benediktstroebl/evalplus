import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    curr, minSum = nums[0], nums[0]
    minDict = {curr: 0}
    for i in range(1, len(nums)):
        curr += nums[i]
        if curr < nums[i]:
            curr = nums[i]
            if minDict[curr] == 0:
                minDict[curr] = i
        minSum = min(minSum, minDict[curr])
    if minSum == len(nums):
        minSum = -1
    return minSum
