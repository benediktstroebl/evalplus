import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # This is similar to a kadane's algorithm problem
    if not nums:
        return 0
    sum = 0
    minimum = math.inf
    for i in range(len(nums)):
        sum += nums[i]
        minimum = min(sum, minimum)
        if sum < 0:
            sum = 0
    return minimum
