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
    right = len(nums) - 1
    curr = nums[left]
    while left < right:
        while curr < 0:
            curr += right - left
        while curr >= nums[right]:
            curr -= nums[left] + right - left
        left += 1
        curr += 1
    return curr
