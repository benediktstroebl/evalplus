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
        if mid == 1:
            left = mid + 1
            if nums[mid] < 0:
                right = mid - 1
        else:
            if nums[mid] > 0:
                left = mid + 1
            else:
                right = mid - 1
    return left
