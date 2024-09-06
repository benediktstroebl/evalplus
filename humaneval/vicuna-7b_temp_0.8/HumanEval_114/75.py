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
    right = max(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[left] + nums[mid] >= mid + nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left
