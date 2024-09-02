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
    left, right = 0, n - 1
    curSum = nums[0]
    minSum = math.inf

    while left <= right:
        if curSum <= 0:
            curSum += nums[right]
            right -= 1
        else:
            curSum -= nums[left]
            left += 1

        minSum = min(minSum, curSum)

    return minSum
