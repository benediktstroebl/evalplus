import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sum = 0
    # max = 0
    # for i in range(len(nums)):
    #     sum = sum + nums[i]
    #     max = max if max > sum else sum
    # return max

    if len(nums) == 0:
        return 0

    min_sub_sum = nums[0]
    min_sum = nums[0]
    for i in range(1, len(nums)):
        min_sum = min_sum + nums[i] if min_sum > nums[i] else nums[i]
        min_sub_sum = min_sum if min_sum < min_sub_sum else min_sub_sum

    return min_sub_sum


