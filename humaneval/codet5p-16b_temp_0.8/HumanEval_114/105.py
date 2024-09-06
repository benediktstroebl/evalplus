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
    minSum = math.inf
    left = 0
    right = 0
    sum = 0
    while right < len(nums):
        sum += nums[right]
        right += 1
        while sum >= minSum:
            minSum = min(minSum, sum)
            sum -= nums[left]
            left += 1
    return minSum
