import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if mid == 0:
            return 0
        elif nums[left] < 0 or nums[mid] < 0 or nums[mid] + nums[left] < 0:
            left = mid + 1
        else:
            right = mid
    return 0
