import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # if len(nums) == 1:
    #     return nums[0]
    # sum = 0
    # min_sum = 999999
    # start, end = 0, 0
    # for i in range(len(nums) - 1):
    #     for j in range(len(nums) - i):
    #         sum = 0
    #         for k in range(j, j + i + 1):
    #             sum += nums[k]
    #         if sum < min_sum:
    #             min_sum = sum
    #             start, end = j, j + i + 1
    # return nums[start:end]

    if len(nums) == 1:
        return nums[0]
    min_sum = 999999
    min_start = 0
    min_end = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum > min
