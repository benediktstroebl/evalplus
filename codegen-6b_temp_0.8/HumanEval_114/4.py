import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    size = len(nums)
    if size == 0:
        return 0
    running_sum = 0
    min_sub_array_sum = nums[0]
    for i in range(size):
        running_sum += nums[i]
        if running_sum < min_sub_array_sum:
            min_sub_array_sum = running_sum
        if running_sum < 0:
            running_sum = 0
    return min_sub_array_sum

