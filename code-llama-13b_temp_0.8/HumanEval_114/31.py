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
    minSum = sum(nums)
    minSumI = None
    for i in range(len(nums)):
        if i == 0:
            minSumI = nums[0]
        else:
            minSumI += nums[i]
        if minSumI < minSum:
            minSum = minSumI
    return minSum
