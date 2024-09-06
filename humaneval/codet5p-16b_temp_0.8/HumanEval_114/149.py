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
    windowSum, curSum = 0, 0
    for n in nums:
        curSum += n
        windowSum = min(windowSum, curSum)
        if curSum < 0:
            curSum = 0
    return windowSum
