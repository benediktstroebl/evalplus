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

    minSubArray = math.inf
    curSubArray = 0
    for i in range(len(nums)):
        curSubArray += nums[i]
        if curSubArray < minSubArray:
            minSubArray = curSubArray
        if curSubArray < 0:
            curSubArray = 0

    return minSubArray
