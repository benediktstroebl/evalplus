import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    maximum = 0
    minimum = 0
    for i, num in enumerate(nums):
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        if maximum == minimum:
            return maximum
        if i > 0:
            minimum = min(minimum, num + nums[i - 1] - nums[i - 2])
    return minimum
