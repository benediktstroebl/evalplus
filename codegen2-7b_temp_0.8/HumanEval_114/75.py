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
    minStart = 0
    
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum < minSum:
                minSum = sum
                minStart = i
            if sum >= minSum:
                break
    return min
