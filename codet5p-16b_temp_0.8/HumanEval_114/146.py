import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = math.inf
    n = len(nums)
    total = 0
    l, r = 0, 0
    while r < n:
        total += nums[r]
        r += 1
        while total >= n:
            min_sum = min(min_sum, total-nums[l])
            total -= nums[l]
            l += 1
    return min_sum

