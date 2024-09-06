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
        return 0
    
    left_sum = nums[0]
    right_sum = nums[-1]
    for i in range(1, len(nums)):
        right_sum += nums[i]
    
    left_sum_sum = sum(nums[0:])
    right_sum_sum = sum(nums[-1:])
    if left_sum_sum < right_sum_sum:
        return left_sum_sum
    else:
        return right_sum_sum
