import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = math.inf
    sum_nums = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            sum_nums += nums[i]
        if i == len(nums) - 1 or sum_nums < result:
            result = min(result, sum_nums)
        elif nums[i + 1] < 0:
            sum_nums += nums[i + 1]
    return result
