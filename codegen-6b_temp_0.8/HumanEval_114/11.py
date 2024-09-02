import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = nums[0]
    min_sum_index = 0

    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
        if nums[i] < min_sum:
            min_sum = nums[i]
            min_sum_index = i

    return min_sum_index
