import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # nums = [-1, -2, -3]
    # min_sum = 0
    # min_sum_idx = 0
    #
    # for i in range(len(nums)):
    #     min_sum += nums[i]
    #     if min_sum < min_sum_idx or min_sum_idx == 0:
    #         min_sum_idx = i
    #     if min_sum < 0:
    #         min_sum = 0
    #
    # return min_sum_idx, min_sum
    #
    # 我的思路是错误的

    # if not nums:
    #     return -1

    min_sum = math.inf
    min_sub_arr = []
    for i in range(len(nums)):
        # if nums[i] < 0:
        #     return -1
        if min_sum < nums[i]:
            return i + 1

        min_sum += nums[i]

    return len(num
