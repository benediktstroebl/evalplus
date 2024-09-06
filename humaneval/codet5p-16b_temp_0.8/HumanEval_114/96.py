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
    minSum = math.inf
    totalSum = 0
    start = 0
    end = 0
    for start in range(n):
        totalSum += nums[start]
        while end < n:
            if totalSum >= minSum:
                break
            else:
                totalSum += nums[end]
                end += 1

        if totalSum < minSum:
            minSum = totalSum

        if end >= n:
            break

        totalSum -= nums[start]

    return minSum


