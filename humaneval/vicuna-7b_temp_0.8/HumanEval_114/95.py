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
        if nums[i] > nums[left]:
            right = i
        else:
            left = i + 1
    result = nums[left] + nums[right]
    for i in range(2, len(nums)):
        if nums[i] > nums[left]:
            right = i
        else:
            left = i + 1
    result = min(result, nums[left] + nums[right])
    return result

nums = [100, 20, 30, 40, 50, 60]
