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
    left, right = 0, 0
    currentSum = 0
    while right < len(nums):
        currentSum += nums[right]
        while currentSum < minSum:
            minSum = currentSum
            left += 1
            currentSum -= nums[left - 1]
        right += 1
    return minSum
