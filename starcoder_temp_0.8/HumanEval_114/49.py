import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    minSum, currentSum = math.inf, 0
    left = 0
    for right in range(len(nums)):
        currentSum += nums[right]
        while currentSum >= minSum:
            minSum = currentSum
            left += 1
            currentSum -= nums[left - 1]

    return minSum
