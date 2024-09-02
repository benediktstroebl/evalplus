import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return
    sum = 0
    min = nums[0]
    for i in range(len(nums)):
        if sum > 0:
            sum += nums[i]
            if sum < min:
                min = sum
        else:
            sum = nums[i]
            if sum < min:
                min = sum
    return min

