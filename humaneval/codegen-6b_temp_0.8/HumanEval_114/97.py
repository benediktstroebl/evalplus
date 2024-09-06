import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums or len(nums) <= 0:
        return 0

    # if only one element, return that element
    if len(nums) == 1:
        return nums[0]

    result = nums[0]
    summation = 0

    for i in range(len(nums)):
        summation += nums[i]
        result = min(summation, result)
        if summation < 0:
            summation = 0

    return result
