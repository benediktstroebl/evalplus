import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    l, r = 0, 0
    s = sum(nums)
    result = s

    while r < len(nums):
        while r < len(nums) and s >= 0:
            s -= nums[r]
            r += 1

        while l < r and s < 0:
            s += nums[l]
            l += 1
            if s < 0:
                result = min(result, s)

    return result if result < 0 else 0

