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
    subArraySum = 0
    index = 0

    for i in range(0, len(nums)):
        subArraySum += nums[i]
        while subArraySum >= minSum and index <= i:
            minSum = min(minSum, subArraySum - minSum)
            index += 1
            subArraySum -= nums[index - 1]
    return minSum
