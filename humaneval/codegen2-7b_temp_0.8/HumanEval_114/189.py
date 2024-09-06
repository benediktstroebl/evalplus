import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = float('inf')
    cur = 0
    ret = 0
    for i, n in enumerate(nums):
        cur += n
        ret = min(ret, cur)
        while cur >= ret:
            total = min(total, ret)
            cur -= nums[i]
            ret += nums[i]
    return
