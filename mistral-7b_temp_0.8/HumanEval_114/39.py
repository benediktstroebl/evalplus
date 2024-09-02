import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # O(n) time | O(1) space
    if len(nums) == 0:
        return 0
    minSum = sum(nums[0:1])
    minStartIdx = 0
    for i in range(1, len(nums)):
        if minSum > nums[i]:
            minSum = nums[i]
            minStartIdx = i
        else:
            minSum = minSum + nums[i]
    return minSum

