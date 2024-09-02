import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #nums[n-1] + nums[n-2] + nums[n-3] +... + nums[0]
    #sliding window
    #O(n) time
    #O(1) space
    n = len(nums)
    sums = [0 for _ in range(n)]
    sums[0] = nums[0]
    totalSum = sums[0]
    for i in range(1, n):
        sums[i] = nums[i] + sums[i-1]
        if sums[i] < nums[i]:
            sums[i] = nums[i]
        if sums[i] < totalSum:
            totalSum = sums[i]
    return totalSum
