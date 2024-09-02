import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    subArraysSum = math.inf
    start = 0
    end = 0
    curSum = 0
    for i in range(len(nums)):
        curSum += nums[i]
        while curSum >= sum(nums[start:end+1]):
            subArraysSum = min(subArraysSum, sum(nums[start:end+1]))
            curSum -= nums[start]
            start += 1
        end += 1
    return subArraysSum

