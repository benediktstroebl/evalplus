import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sub_sum = sum(nums)
    min_sub_sum = sub_sum

    for num in nums:
        sub_sum = sub_sum - num
        min_sub_sum = min(min_sub_sum, sub_sum)

    return min_sub_sum
