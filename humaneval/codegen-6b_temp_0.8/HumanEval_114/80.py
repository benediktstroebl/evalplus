import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = sum(nums)
    if minSum == 0:
        return 0
    n = len(nums)
    s = []
    for i in range(n):
        while s and nums[i] >= nums[s[-1]]:
            s.pop()
        s.append(i)
    for i in range(n-1):
        minSum -= nums[i]
        while s and minSum >= nums[s[-1]]:
            minSum -= nums[s.pop()]
    return minSum
