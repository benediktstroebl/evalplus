import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_so_far = 0
    min_sub_array_sum = math.inf
    for i in range(len(nums)):
        sum_so_far = max(nums[i], sum_so_far + nums[i])
        min_sub_array_sum = min(sum_so_far, min_sub_array_sum)

    return min_sub_array_sum
