import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # A subarray of length 1 is defined to have a minimum sum of its only element.
    minSum = nums[0]
    # nums[1:] is the list of subarrays with length at least 2.
    for i in range(1, len(nums)):
        subArrSum = sum(nums[i:])
        if subArrSum < minSum:
            minSum = subArrSum
    return minSum
