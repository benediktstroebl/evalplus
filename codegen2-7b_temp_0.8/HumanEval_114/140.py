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
    for i in range(1, len(nums)):
        sum_of_sub_array = 0
        for j in range(i):
            sum_of_sub_array += nums[j]
        if sum_of_sub_array < min_sub_array_sum:
            min_sub_array_sum = sum_of_sub_array
