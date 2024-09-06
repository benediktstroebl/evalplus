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
    left = 0
    for i, num in enumerate(nums):
        if left == i:
            minSum = min(minSum, num)
        else:
            minSum = min(minSum, num + left)
        left += num

    return minSum if minSum < math.inf else -1
