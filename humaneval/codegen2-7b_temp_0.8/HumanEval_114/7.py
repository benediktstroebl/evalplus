import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    res = nums[0]
    res_sum = nums[0]

    for i in range(1, len(nums)):
        res_sum += nums[i]
        if res_sum < nums[i]:
            res = res_sum
        elif res_sum >= nums[i]:
            res = min(res, res_sum)

    return
