import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    cur_min = 0
    cur_max = math.inf
    min_sum = math.inf
    for i in range(len(nums)):
        cur_min = cur_min if nums[i] > cur_min else nums[i]
        cur_max = cur_max if cur_max < cur_min + nums[i] else cur_min + nums[i]
        if cur_max < min_sum:
            min_sum = cur_max
    return min_sum
