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
        if currentSum < minSum:
            minSum = currentSum

        right += 1

    if right == len(nums):
        currentSum = 0
        right -= 1
        left = 0

    while right >= left:
        currentSum += nums[right]
        currentSum -= nums[left]
        if currentSum < minSum:
            minSum = currentSum

        right -= 1
        left += 1

    return minSum

