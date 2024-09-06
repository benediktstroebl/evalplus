import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # minSubArraySum([-1, -2, -3]) == -6
    # minSubArraySum([1, 4, 4]) == 1
    # minSubArraySum([0, 3, 5]) == 0
    # minSubArraySum([-1, 1, 2]) == 2
    # minSubArraySum([-1, -3, 2, 3, 1]) == -2
    # minSubArraySum([-1, -3, 2, 3, 1]) == -2
    # minSubArraySum([-2, -1, -2, -1, -2]) == -1
    # minSubArraySum([1, 1, 1, 1]) == 1
    # minSubArraySum([2, 1, 2, 1, 1]) == 2
    # minSubArraySum([2, 1, 1, 1, 1]) == 1
