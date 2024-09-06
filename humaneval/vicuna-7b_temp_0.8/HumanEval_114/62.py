import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sort the array
    nums = sorted(nums)
    # initialize sum to 0 and start index to 0
    sum = 0
    start = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            return -1
        sum += nums[i]
        if nums[i] == 0:
            start = i
    # return the minimum sum of the sub-array
    return sum - start
