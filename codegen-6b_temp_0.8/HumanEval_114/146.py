import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = 0
    min_sum_arr = nums[:]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            min_sum = 0
            for k in range(i, j):
                min_sum += nums[k]
            if min_sum < min_sum_arr[i]:
                min_sum_arr[i] = min_sum
    return min(min_sum_arr)
