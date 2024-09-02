import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, nums[0]
    for i in range(1, len(nums)):
        if nums[i] < nums[left]:
            left = i
        if nums[i] > nums[right]:
            right = i
    if right - left + 1 == 0:
        return 0
    return left + right - 1
