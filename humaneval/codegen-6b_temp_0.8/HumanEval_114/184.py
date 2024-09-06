import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    
    start = 0
    end = 0
    minSum = math.inf
    currSum = 0
    
    while end < len(nums):
        if currSum < 0:
            if end - start <= 1:
                if minSum > currSum:
                    minSum = currSum
            currSum = nums[end]
            end += 1
        else:
            currSum += nums[end]
            end += 1
    
    if minSum > currSum:
        return minSum
    else:
        return currSum
