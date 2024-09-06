import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # minSum = math.inf
    # start = 0
    # while start < len(nums):
    #     i = start
    #     j = start + 1
    #     while j < len(nums) + 1:
    #         sub_arr_sum = sum(nums[i:j])
    #         if sub_arr_sum < minSum:
    #             minSum = sub_arr_sum
    #         j += 1
    #     start += 1
    # return minSum

    minSum = math.inf
    start = 0
    while start < len(nums):
        sub_arr_sum = 0
        for j in range(start, len(nums)):
            sub_arr_sum += nums[j]
            if sub_arr_sum < minSum:
                minSum = sub_arr_sum
        start += 1
    return minSum


