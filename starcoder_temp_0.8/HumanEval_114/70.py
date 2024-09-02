import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    windowSum = 0
    start = 0
    for end, num in enumerate(nums):
        windowSum += num
        while windowSum >= minSum:
            minSum = min(minSum, windowSum)
            windowSum -= nums[start]
            start += 1

    return minSum if minSum!= math.inf else 0
