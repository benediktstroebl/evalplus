import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    ans = math.inf
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        ans = min(ans, s)
        s = min(s, 0)
    return ans
