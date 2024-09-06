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
    sub = []
    sum = 0
    for i in range(n):
        sum += nums[i]
        sub.append(sum)

    min = sub[0]
    for i in range(1, n):
        min = min if min < sub[i] - nums[i-1] else sub[i] - nums[i-1]

    return min

