import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def minSubArraySumSub(nums, target):
        total = math.inf
        for start in range(len(nums)):
            total = min(total, sum(nums[start:]) - target)
        return total
    return minSubArraySumSub(nums, sum(nums))
