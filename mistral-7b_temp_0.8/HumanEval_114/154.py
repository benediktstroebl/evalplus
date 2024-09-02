import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_nums = 0
    min_num = math.inf
    # 注意数组长度为1时，不需要判断
    for i in range(len(nums)):
        sum_nums = sum_nums + nums[i]
        min_num = min(sum_nums, min_num)
        if sum_nums < 0:
            sum_nums = 0
    return min_num
