import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0

    def helper(nums, curr, start, min_sum):
        if start >= len(nums):
            return min_sum
        curr += nums[start]
        min_sum = min(curr, min_sum)
        return helper(nums, curr, start + 1, min_sum)

    return helper(nums, 0, 0, math.inf)

