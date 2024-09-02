import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = float('inf')
    min_sub_arr = []
    sub_arr = []

    for i in range(len(nums)):
        sub_arr.append(nums[i])
        if len(sub_arr) == 1:
            min_sum = nums[i]
            min_sub_arr = [nums[i]]
            continue
        curr_sum = sum(sub_arr)
        if curr_sum < min_sum:
            min_sum = curr_sum
            min_sub_arr = sub_arr
    return min_sub_arr, min_sum
