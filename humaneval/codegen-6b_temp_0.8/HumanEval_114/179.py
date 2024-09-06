import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_array_sum = sys.maxint
    current_array_sum = 0
    for i in range(len(nums)):
        current_array_sum += nums[i]
        if current_array_sum < 0:
            current_array_sum = 0
        elif current_array_sum < min_array_sum:
            min_array_sum = current_array_sum

    return min_array_sum

