import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n == 0:
        return 0

    min_sum = float("inf")
    total = 0
    left, right = 0, 0
    while right < n:
        total += nums[right]
        min_sum = min(min_sum, total)
        right += 1
        while left < n and total > min_sum:
            total -= nums[left]
            left += 1

    return min_sum

