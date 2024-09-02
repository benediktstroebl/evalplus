import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = sum(nums)
    minSumMap = {minSum:[]}
    for i in range(0,len(nums)):
        minSum += nums[i]
        minSumMap[minSum] = minSumMap.get(minSum,[]) + [i + 1]
    return minSumMap.get(0,[]) # Trying to return the first element with 0 as a key


