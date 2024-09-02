import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) <= 0:
        return 0

    l = len(nums)
    cur_min = nums[0]

    for i in range(1, l):
        cur_min = min(cur_min, cur_min - nums[i-1] + nums[i])
        if cur_min < 0:
            cur_min = nums[i]

    return cur_min
