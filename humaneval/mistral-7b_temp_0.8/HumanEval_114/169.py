import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # set min
    min = nums[0]
    # set submin
    submin = 0
    # set minindex
    minindex = 0

    for i in range(len(nums)):
        if nums[i] < submin:
            submin = nums[i]
            minindex = i

        if submin < min:
            min = submin

    return min, minindex

