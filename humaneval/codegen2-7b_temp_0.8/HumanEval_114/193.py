import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    low = 0
    high = 0
    cur = 0
    sum = 0
    res = math.inf

    for i in range(0, len(nums)):
        cur = cur + nums[i]
        if cur < 0:
            cur = 0
        if sum < cur:
            sum = cur
            low = i
        if sum > res:
            res = sum
    return res
