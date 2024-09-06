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

    left = 0
    right = 0
    min_sum = math.inf
    s = 0

    while right < n:
        s += nums[right]
        right += 1

        if s < min_sum:
            min_sum = s

        while s >= min_sum:
            s -= nums[left]
            left += 1

    return min_sum
