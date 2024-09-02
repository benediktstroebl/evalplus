import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    min_num = math.inf
    min_sub_sum = math.inf

    for num in nums:
        min_num = num if num < min_num else min_num
        min_sub_sum = num + min_num if num + min_num < min_sub_sum else min_sub_sum

    return min_sub_sum

