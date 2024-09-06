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
    min_sum = math.inf
    for i in range(n):
        sum_nums = 0
        for j in range(i, n):
            sum_nums += nums[j]
            if sum_nums < min_sum:
                min_sum = sum_nums
    return min_sum
