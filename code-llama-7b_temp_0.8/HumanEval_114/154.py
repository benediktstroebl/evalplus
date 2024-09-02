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
    s = [0 for i in range(n)]
    for i in range(1, n):
        s[i] = s[i - 1] + nums[i]
    for i in range(n):
        for j in range(i + 1, n):
            subarray = s[j] - s[i]
            if subarray < 0:
                break
            min_sum = min(subarray, min_sum) if min_sum else subarray
    return min_sum
