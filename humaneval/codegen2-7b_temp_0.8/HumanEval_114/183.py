import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = min(nums)
    sum_so_far = sum
    cur_sum = sum
    for i in range(len(nums)):
        if sum_so_far > 0:
            cur_sum += nums[i]
        else:
            sum_so_far = nums[i]
        sum_so_far = min(sum_so_far, cur_sum)
    return
