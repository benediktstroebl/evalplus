import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums or len(nums) == 0:
        return 0
    
    n = len(nums)
    minSum = sum(nums[:n])
    curSum = minSum
    for i in range(1, n):
        curSum = curSum - nums[i - 1] + nums[i + n - 1]
        minSum = min(minSum, curSum)
    
    return minSum

