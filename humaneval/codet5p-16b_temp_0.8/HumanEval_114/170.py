import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    length = len(nums)
    if length == 0:
        return -1
    
    minSum = math.inf
    for i in range(0, length):
        sum = 0
        for j in range(i, length):
            sum += nums[j]
            if sum < minSum:
                minSum = sum
            if sum >= 0:
                break
    return minSum
