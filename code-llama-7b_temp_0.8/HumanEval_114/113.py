import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    start, end = 0, len(nums) - 1
    best = nums[0]
    total = 0

    for num in nums:
        total += num
        best = min(best, total)

        if total < 0:
            total = 0
        else:
            best = min(best, total)
    return best

