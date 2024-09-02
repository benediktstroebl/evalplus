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
    # sum_current = 0
    #
    # for i in range(len(nums)):
    #     sum_current += nums[i]
    #     if sum_current > 0:
    #         min_sum = min(min_sum, sum_current)
    #     else:
    #         min_sum = min(min_sum, 0)
    # return min_sum
    min_sum = 0
    for i in range(len(nums)):
        sum_current = 0
        if i == 0:
            sum_current = nums[0]
            if sum_current > 0:
                min_sum = min(min_sum, sum_current)
            else:
                min_sum = min(min_sum, 0)
        else:
            sum_current = nums[i] + sum_current
            if sum_current > 0:
                min_sum = min(min_sum, sum_current)
            else:
               
