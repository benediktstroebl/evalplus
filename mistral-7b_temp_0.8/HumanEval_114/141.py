import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0

    min_sum = nums[0]
    min_len = 0

    sum_nums = nums[0]
    sum_len = 1

    for i in range(1, len(nums)):
        sum_nums = sum_nums - nums[i-1] + nums[i]
        if sum_nums > 0:
            sum_len = sum_len + 1
        else:
            if sum_nums < min_sum:
                min_sum = sum_nums
                min_len = sum_len
            sum_len = 1
            sum_nums = nums[i]

    return min_len
