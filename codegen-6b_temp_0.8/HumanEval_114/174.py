import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    N = len(nums)
    res = []
    for i in range(N):
        for j in range(i, N):
            res.append(sum(nums[i:j+1]))
    return min(res)
