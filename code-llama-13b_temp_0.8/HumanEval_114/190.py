import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]

    current_total = sum(nums)
    min_total = current_total
    for i in range(1, len(nums)):
        current_total -= nums[i - 1]
        min_total = min(current_total, min_total)

    return min_total
