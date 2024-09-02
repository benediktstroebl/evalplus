import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def min_sum(nums):
        l = len(nums)
        if l == 0: return math.inf
        if l == 1: return nums[0]
        return min(nums[0] + minSubArraySum(nums[1:]), min_sum(nums[1:]))
    return min_sum(nums)
