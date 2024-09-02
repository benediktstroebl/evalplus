import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    windowSum = 0
    minSum = nums[0]
    start = 0

    for end, num in enumerate(nums, 1):
        windowSum += num

        while windowSum >= minSum:
            windowSum -= nums[start]
            start += 1

        minSum = min(minSum, windowSum)

    return minSum
