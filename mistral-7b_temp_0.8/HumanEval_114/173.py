import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    sum_nums = 0
    min_start = 0
    for i in range(len(nums)):
        sum_nums += nums[i]
        if sum_nums > min_sum:
            sum_nums -= nums[min_start]
            min_start += 1
        elif sum_nums < min_sum:
            min_start = i
            min_sum = sum_nums
    return min_sum
