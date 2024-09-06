import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sub_array = float('inf')
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if i > 0 and current_sum > min_sub_array:
            break
        if current_sum < min_sub_array:
            min_sub_array = current_sum
    return min_sub_array
