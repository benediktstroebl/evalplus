import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return -1
    for i in range(1, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < nums[i+1]:
                return nums[i] + nums[j]
    return -1
