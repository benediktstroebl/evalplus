import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    subArray = nums[0]
    minSubArray = subArray
    for i in range(1, len(nums)):
        subArray = subArray + nums[i]
        if subArray < minSubArray:
            minSubArray = subArray
        elif subArray > 0:
            subArray = nums[i]
    return minSubArray
