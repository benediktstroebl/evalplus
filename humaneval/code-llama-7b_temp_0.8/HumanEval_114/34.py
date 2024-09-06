import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    start = 0
    sum = 0
    minSum = math.inf
    for end in range(len(nums)):
        sum += nums[end]
        minSum = min(minSum, sum - nums[start])
        while sum < 0 and start < len(nums) - 1:
            start += 1
            sum += nums[start]

        minSum = min(minSum, sum - nums[start])

    return minSum
