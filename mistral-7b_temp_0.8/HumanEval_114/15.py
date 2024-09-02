import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # for i in range(len(nums)):
    #     sub = sum(nums[i:])
    #     print(sub)
    #     return sub

    # counter = 0
    # current_min = nums[0]
    # for i in range(len(nums)):
    #     counter += nums[i]
    #     if counter > current_min:
    #         current_min = counter
    #     if counter < 0:
    #         counter = 0
    # print(current_min)
    # return current_min

    # for i in range(1, len(nums)):
    #     nums[i] += nums[i - 1]
    # print(nums)
    #
    #
    # counter = 0
    # current_min = nums[0]
    # for i in range(len(nums)):
    #     counter += nums[i]
    #     if counter < current_min:
    #         current_min = counter
    #     if counter
