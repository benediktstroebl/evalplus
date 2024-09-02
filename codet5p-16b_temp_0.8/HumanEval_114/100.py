import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = math.inf
    start, end = 0, 0
    current_total = 0

    for i in range(len(nums)):
        current_total += nums[i]

        while current_total >= total:
            total = min(current_total, total)
            start = i
            current_total -= nums[start]

    return total
