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
    for i in range(1, len(nums)):
        right = math.ceil((nums[i] + nums[i+1])/2)
        if nums[left] + nums[right-1] < nums[i]:
            left = right - 1
    return left
