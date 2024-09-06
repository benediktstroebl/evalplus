import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    left = 0
    right = len(nums)
    minSum = math.inf
    while left < right:
        if left == 0:
            minSum = min(minSum, sum(nums[left:right]))
        else:
            minSum = min(minSum, sum(nums[left:right]))
            minSum = min(minSum, sum(nums[0:left+1]))
        left += 1
    return minSum
