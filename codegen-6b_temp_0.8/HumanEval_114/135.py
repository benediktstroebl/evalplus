import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    
    min_sum = nums[0]
    cur_sum = nums[0]
    for i in range(1, n):
        cur_sum = max(nums[i], cur_sum + nums[i])
        min_sum = min(min_sum, cur_sum)
    return min_sum
