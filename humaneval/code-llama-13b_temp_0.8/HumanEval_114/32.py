import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total_length = len(nums)
    result = sum(nums)
    minimum = math.inf
    for i in range(total_length):
        result -= nums[i]
        minimum = min(result, minimum)
        result += nums[i]

    return minimum

