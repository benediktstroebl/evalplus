import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, 1
    for i in range(len(nums)):
        right = max(nums[i+1], right)
        if nums[i] == 0:
            if left <= right-left:
                left = left + 1
        else:
            if left <= right-left+nums[i]:
                left = left + 1
    return left
