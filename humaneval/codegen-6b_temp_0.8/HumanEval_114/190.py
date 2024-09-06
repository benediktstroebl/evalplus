import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # if not nums:
    #     return 0
    # min_sum = nums[0]
    # min_sum_index = 0
    # for i in range(len(nums)):
    #     curr_sum = 0
    #     for j in range(i, len(nums)):
    #         curr_sum += nums[j]
    #         if min_sum < curr_sum:
    #             min_sum = curr_sum
    #             min_sum_index = i
    # return min_sum
    if not nums:
        return 0

    min_sum = nums[0]
    min_sum_index = 0
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        if min_sum > curr_sum:
            min_sum = curr_sum
            min_sum_index = i
    return min_sum

