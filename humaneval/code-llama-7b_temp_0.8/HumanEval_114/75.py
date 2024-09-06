import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    sub_sum = nums[0]
    min_sub_sum = sub_sum
    for i in range(1, len(nums)):
        sub_sum = max(nums[i], sub_sum + nums[i])
        if sub_sum < min_sub_sum:
            min_sub_sum = sub_sum
    return min_sub_sum
