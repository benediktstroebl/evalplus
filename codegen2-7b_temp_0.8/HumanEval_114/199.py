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
    if n == 1:
        return nums[0]
    min_sum = float("inf")
    for i in range(n):
        temp = nums[i]
        cur_sum = 0
        for j in range(i,n):
            cur_sum += nums[j]
            min_sum = min(min_sum, cur_sum)
