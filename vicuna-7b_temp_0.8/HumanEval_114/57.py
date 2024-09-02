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
    result = float('inf')
    for i in range(1, len(nums)):
        if nums[i] < left:
            break
        else:
            left = nums[i]
            sub_result = result + left
            if sub_result < result:
                result = sub_result
        if nums[i] - left < right:
            right = nums[i] - left
    return result
