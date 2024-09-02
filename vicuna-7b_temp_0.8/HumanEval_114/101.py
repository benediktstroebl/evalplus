import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = nums[0]
    right = nums[-1]
    sum = 0
    for i in range(1, len(nums)):
        if nums[i] >= right:
            break
        sum += nums[i]
        if sum < left:
            return sum
    return sum
