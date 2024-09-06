import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums.sort()
    i = 0
    result = nums[0] + nums[0]
    while i < len(nums) - 1:
        if nums[i] + nums[i+1] <= 0:
            break
        result = min(result, nums[i] + nums[i+1])
        i += 1
    return result
