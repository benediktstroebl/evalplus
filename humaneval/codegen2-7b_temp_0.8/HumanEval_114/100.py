import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sub_array_sum = math.inf
    for sub_array_start in range(len(nums)):
        sum = 0
        for sub_array_end in range(sub_array_start, len(nums)):
            sum += nums[sub_array_end]
            if sum >= min_sub_array_sum:
                min_sub_array_sum = sum
    return min_sub_
