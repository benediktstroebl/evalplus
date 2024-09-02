import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # return min(sum(nums[i:j+1]) for i in range(len(nums)) for j in range(i, len(nums)))
    i, j, res = 0, 0, math.inf
    while j < len(nums):
        res = min(res, nums[j] + (j - i + 1) * res)
        j += 1
    return res

