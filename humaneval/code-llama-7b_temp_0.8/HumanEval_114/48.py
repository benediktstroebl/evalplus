import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = sum(nums)
    if len(nums) == 1:
        return result

    minSum = math.inf
    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
        minSum = min(temp, minSum)
        if temp < 0:
            temp = 0
    return minSum
