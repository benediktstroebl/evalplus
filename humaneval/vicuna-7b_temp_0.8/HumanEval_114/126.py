import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = nums[0]
    right = max(nums)
    min_sum = math.inf
    for i in range(1, len(nums)):
        right = max(nums[i], right)
        if right - left <= 0:
            return 0
        left = nums[i]
        sum = left + (right - left)
        if sum < min_sum:
            min_sum = sum
    return min_sum
