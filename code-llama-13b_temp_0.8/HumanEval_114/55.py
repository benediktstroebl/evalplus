import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def slidingWindow(nums, windowSize):
        windowStart, windowSum, minSum = 0, 0, math.inf

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]

            if windowEnd >= windowSize - 1:
                minSum = min(minSum, windowSum)
                windowSum -= nums[windowStart]
                windowStart += 1

        return minSum

    return min(slidingWindow(nums, windowSize) for windowSize in range(1, len(nums) + 1))
