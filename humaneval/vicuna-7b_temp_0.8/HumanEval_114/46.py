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
    for i in range(len(nums) - 1):
        right = math.min(nums[i], nums[i+1])
        if right - left >= nums[i]:
            return left + right
        left = right
    return left + nums[len(nums)-1]

nums = [2, 3, 4, 1, 2, 4]
