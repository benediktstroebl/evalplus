import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sums = 0
    minSum = math.inf
    left, right = 0, 0
    while right < len(nums):
        sums += nums[right]
        while sums >= minSum:
            minSum = sums
            left = right
            sums -= nums[left]
        right += 1
    return minSum
