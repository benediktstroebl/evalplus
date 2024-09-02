import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = nums[0]
    if len(nums) == 1:
        return result
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            new_result = sum(nums[i:j+1])
            if new_result < result:
                result = new_result
    return result
