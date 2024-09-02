import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    curSum = nums[0]
    minSum = curSum
    for num in nums[1:]:
        curSum = min(curSum + num, num)
        minSum = min(minSum, curSum)
    return minSum
