import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = sum(nums)
    for i in range(1, len(nums)):
        curr_sum = sum(nums[:i])
        if curr_sum > max_sum:
            continue
        if curr_sum == max_sum:
            min_sub_array_sum = curr_sum
            min_index = i
        else:
            min_sub_array_sum = min(curr_sum, minSubArraySum(nums[i:]))
            min_index = i
    return min_sub_array_sum
